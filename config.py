import os

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True

class Production(Config):
    DEBUG = True

class Stage(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class Testing(Config):
    TESTING = True
    
