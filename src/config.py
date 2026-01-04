import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    GEMINI_3_MODEL = os.environ.get('GEMINI_3_MODEL')
    GEMINI_2_5_MODEL = os.environ.get('GEMINI_2_5_MODEL')
    CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH')
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}