from os import environ, path
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'guess-what-it-is'
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or  'sqlite:///' + path.join(basedir, 'myshop.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False