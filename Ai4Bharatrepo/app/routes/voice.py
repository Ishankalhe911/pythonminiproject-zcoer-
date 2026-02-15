from flask import Blueprint, request, Response
from twilio.twiml.voice_response import VoiceResponse, Record
from datetime import datetime
import threading

from app.services.ai_service import (
    save_callback_request,
    download_audio,
    transcribe_audio_to_hindi,
    generate_ai_answer
)

bp = Blueprint('voice', __name__, url_prefix='/voice')


# -------------------------------
# STEP 1 — INITIAL CALL
# -------------------------------
@bp.route('/', methods=['POST'], strict_slashes=False)
def initial_call():
    resp = VoiceResponse()

    resp.say(
        "नमस्ते! ग्रामीण AI वॉइस सिस्टम। आपको 30 सेकंड मिलेंगे अपना सवाल बताने के लिए। "
        "हम 5 मिनट में आपको कॉलबैक करेंगे। तैयार हैं?",
        language='hi-IN'
    )

    record = Record(
        action='/voice/recording-complete',
        timeout=30,
        max_length=30,
        finish_on_key='#',
        play_beep=True
    )

    resp.append(record)

    flask_resp = Response(str(resp), mimetype='text/xml')
    flask_resp.headers['ngrok-skip-browser-warning'] = 'true'

    return flask_resp


# -------------------------------
# BACKGROUND PROCESSING
# -------------------------------
def process_ai_background(phone, recording_url):
    try:
        print(f"🤖 Background AI processing for {phone}")

        # Download audio (now unique per user)
        local_file = download_audio(recording_url)
        if not local_file:
            print("❌ Audio download failed. Skipping callback.")
            return

        # Transcribe
        user_text = transcribe_audio_to_hindi(local_file)

        if not user_text:
            print("⚠️ Empty transcription. Skipping callback.")
            return

        clean_text = user_text.strip()

        if len(clean_text) < 5:
            print("⚠️ Very short / unclear speech. Skipping callback.")
            return

        # 🔥 PASS PHONE FOR 60 MIN CONTEXT
        ai_answer = generate_ai_answer(clean_text, phone)

        if not ai_answer:
            print("❌ AI answer generation failed. Skipping callback.")
            return

        # 🔥 FIXED PARAMS (no transcript field)
        save_callback_request(
            phone,
            ai_answer,
            datetime.now()
        )

        print("✅ Answer stored for callback")

    except Exception as e:
        print(f"❌ Background processing failed: {e}")


# -------------------------------
# STEP 2 — RECORDING COMPLETE
# -------------------------------
@bp.route('/recording-complete', methods=['POST'], strict_slashes=False)
def recording_saved():
    resp = VoiceResponse()

    caller_phone = request.values.get('From')
    recording_url = request.values.get('RecordingUrl')

    if not caller_phone or not recording_url:
        resp.say(
            "रिकॉर्डिंग प्राप्त नहीं हुई। कृपया दोबारा कॉल करें।",
            language='hi-IN'
        )
        resp.hangup()
        return Response(str(resp), mimetype='text/xml')

    direct_audio_url = f"{recording_url}.wav"

    threading.Thread(
        target=process_ai_background,
        args=(caller_phone, direct_audio_url),
        daemon=True
    ).start()

    resp.say(
        "धन्यवाद! आपका सवाल रिकॉर्ड हो गया। हम 5 मिनट में कॉलबैक करेंगे।",
        language='hi-IN'
    )
    resp.hangup()

    return Response(str(resp), mimetype='text/xml')
