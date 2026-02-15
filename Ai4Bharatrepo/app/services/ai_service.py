import json
import requests
import os
from datetime import datetime, timedelta
from pathlib import Path
from google import genai

# ==============================
# CONFIG
# ==============================

CALL_QUEUE = Path("call_queue.json")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "models/gemini-2.5-flash"


# ==============================
# CALLBACK QUEUE MANAGEMENT
# ==============================

def save_callback_request(phone, ai_answer, timestamp):
    """
    Save final AI answer for scheduled callback (5 mins later)
    """

    data = {
        "phone": phone,
        "answer": ai_answer,
        "created": timestamp.isoformat(),
        "callback_time": (timestamp + timedelta(minutes=5)).isoformat()
    }

    queue = []

    if CALL_QUEUE.exists():
        with open(CALL_QUEUE, "r") as f:
            try:
                queue = json.load(f)
            except json.JSONDecodeError:
                queue = []

    queue.append(data)

    # Multi-user safe ordering
    queue.sort(key=lambda x: datetime.fromisoformat(x["callback_time"]))

    with open(CALL_QUEUE, "w") as f:
        json.dump(queue, f, indent=4)

    return True


def get_pending_callbacks():
    """
    Returns calls where current time >= callback_time
    Removes processed ones
    """

    if not CALL_QUEUE.exists():
        return []

    with open(CALL_QUEUE, "r") as f:
        try:
            queue = json.load(f)
        except json.JSONDecodeError:
            return []

    now = datetime.now()

    pending = [
        call for call in queue
        if datetime.fromisoformat(call["callback_time"]) <= now
    ]

    remaining = [
        call for call in queue
        if datetime.fromisoformat(call["callback_time"]) > now
    ]

    with open(CALL_QUEUE, "w") as f:
        json.dump(remaining, f, indent=4)

    return pending


# ==============================
# 60 MINUTE USER HISTORY
# ==============================

def get_recent_user_history(phone):
    """
    Returns last AI answer if same user called within 60 minutes
    """

    if not CALL_QUEUE.exists():
        return None

    with open(CALL_QUEUE, "r") as f:
        try:
            queue = json.load(f)
        except json.JSONDecodeError:
            return None

    now = datetime.now()

    for call in reversed(queue):
        if call["phone"] == phone:
            created_time = datetime.fromisoformat(call["created"])
            if now - created_time <= timedelta(minutes=60):
                return call["answer"]

    return None


# ==============================
# AUDIO DOWNLOAD (MULTI USER SAFE)
# ==============================

def download_audio(recording_url):
    """
    Download Twilio recording with unique filename
    """

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")

    unique_filename = f"user_query_{datetime.now().timestamp()}.wav"

    response = requests.get(recording_url, auth=(account_sid, auth_token))

    if response.status_code == 200:
        with open(unique_filename, "wb") as f:
            f.write(response.content)
        return unique_filename

    print(f"❌ Failed to download audio: {response.status_code}")
    return None


# ==============================
# TRANSCRIPTION
# ==============================

def transcribe_audio_to_hindi(file_path):
    """
    Convert .wav into Hindi text.
    Returns None if silent / unclear.
    """

    if not file_path or not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "rb") as f:
            audio_bytes = f.read()

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": "Transcribe this audio accurately in Hindi. If silent or unclear, return EMPTY."},
                        {
                            "inline_data": {
                                "mime_type": "audio/wav",
                                "data": audio_bytes
                            }
                        }
                    ]
                }
            ]
        )

        transcript = response.text.strip()

        if not transcript or transcript.upper() == "EMPTY":
            return None

        return transcript

    except Exception as e:
        print(f"❌ Transcription error: {e}")
        return None


# ==============================
# AI RESPONSE GENERATION
# ==============================

def generate_ai_answer(user_text, phone=None):
    """
    Generate Hindi answer.
    Includes 60-min context if exists.
    """

    if not user_text:
        return None

    try:
        previous_context = get_recent_user_history(phone) if phone else None

        prompt = f"""
You are a helpful assistant for rural Indian users.
Give clear, simple, and practical advice in Hindi.
Avoid complex vocabulary.
Be direct and actionable.

Previous conversation (if any):
{previous_context if previous_context else "None"}

User question:
{user_text}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        answer = response.text.strip()

        if not answer:
            return None

        return answer

    except Exception as e:
        print(f"❌ LLM error: {e}")
        return None
