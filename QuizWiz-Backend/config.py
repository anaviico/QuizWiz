import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5433/quizwiz'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
