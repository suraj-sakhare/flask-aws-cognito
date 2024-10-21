import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    COGNITO_POOL_ID = os.getenv('COGNITO_POOL_ID')
    COGNITO_CLIENT_ID = os.getenv('COGNITO_CLIENT_ID')
    COGNITO_CLIENT_SECRET = os.getenv('COGNITO_CLIENT_SECRET')
    COGNITO_DOMAIN = os.getenv('COGNITO_DOMAIN')
    REDIRECT_URI = os.getenv('REDIRECT_URI')
    COGNITO_KEYS_URL = os.getenv('COGNITO_KEYS_URL')
    LOGIN_URL = os.getenv('LOGIN_URL')
    TOKEN_URL = os.getenv('TOKEN_URL')
    LOGOUT_URL = os.getenv('LOGOUT_URL')
