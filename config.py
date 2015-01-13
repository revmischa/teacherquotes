import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    if os.environ.has_key('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = True
    if os.environ.has_key('HEROKU_POSTGRESQL_VIOLET_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ['HEROKU_POSTGRESQL_VIOLET_URL']

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/quotes'


class TestingConfig(Config):
    TESTING = True
