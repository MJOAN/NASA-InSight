import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''

class Production(Config):
    DEBUG = False

class Stage(Config):
    DEVELOPMENT = True
    DEBUG = False
    
class Testing(Config):
    TESTING = True
    
