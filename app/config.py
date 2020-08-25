import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-what-it-is'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///myshop.db'