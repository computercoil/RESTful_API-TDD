import os

class Config(object):
    "Parent config class"
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/test_db"
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
    }