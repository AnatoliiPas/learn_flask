import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('APP_SECRET_KEY')
