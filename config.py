from os import path, environ
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or  'sqlite:///' + path.join(basedir, 'myshop.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email server settings
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = int(environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')