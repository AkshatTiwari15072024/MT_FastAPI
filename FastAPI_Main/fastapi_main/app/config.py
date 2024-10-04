
import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

class Config:
    # Configuration class to manage application settings
    DEBUG = os.getenv('DEBUG') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
