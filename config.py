import os

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
    
