from os import path, getenv
basedir = path.abspath(path.dirname(__file__))


class Config(object):
    SECRET_KEY = getenv('SECRET_KEY')
    # Database
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL') or  'sqlite:///' + path.join(basedir, 'myshop.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email server settings
    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = int(getenv('MAIL_PORT') or 587)
    MAIL_USE_TLS = getenv('MAIL_USE_TLS')
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')