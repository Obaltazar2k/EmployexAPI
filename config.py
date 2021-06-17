
import datetime

class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "Blah!"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)  

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True