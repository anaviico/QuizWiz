class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@db:5432/quizwiz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
