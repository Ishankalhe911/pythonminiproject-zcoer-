import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from app.config import Config
from app.routes import voice
from app.services.ai_service import get_pending_callbacks


def check_callbacks():
    """Background task: Only initiate callback using saved AI answer"""

    pending = get_pending_callbacks()
    if not pending:
        return

    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

    for callback_data in pending:
        phone = callback_data['phone']
        answer = callback_data['answer']

        try:
            print(f"📞 Initiating callback for {phone}")

            # Create TwiML response directly (NO URL PARAMS)
            response = VoiceResponse()
            response.say(
                "नमस्ते! यह ग्रामीण ए आई वॉइस सिस्टम से आपका कॉलबैक है। "
                "आपके सवाल का जवाब इस प्रकार है:",
                language='hi-IN'
            )
            response.say(answer, language='hi-IN')
            response.say("धन्यवाद।", language='hi-IN')
            response.hangup()

            # 🔥 IMPORTANT: Use twiml= NOT url=
            client.calls.create(
                to=phone,
                from_=Config.TWILIO_PHONE_NUMBER,
                twiml=str(response)
            )

            print(f"✅ Callback successful for {phone}")

        except Exception as e:
            print(f"❌ Callback failed for {phone}: {e}")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(voice.bp)

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=check_callbacks, trigger="interval", seconds=30)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
