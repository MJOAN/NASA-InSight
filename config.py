import os
basedir = os.path.abspath(os.path.dirname(__file__))

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class Production(Config):
    DEBUG = False

class Stage(Config):
    DEVELOPMENT = True
    DEBUG = False
    
class Testing(Config):
    TESTING = True
    
