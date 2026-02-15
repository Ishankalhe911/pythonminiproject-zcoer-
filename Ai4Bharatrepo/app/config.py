import os
from dotenv import load_dotenv

# This loads the .env file located in your project root
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
    # Replace with your actual ngrok or public URL
    BASE_URL = os.getenv("BASE_URL", "http://your-ngrok-url.ngrok-free.app")
