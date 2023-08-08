import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class appConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(appConfig):
    DEBUG = True
    PORT = 3000
    
    server = 'localhost'
    username = 'root'
    password = 'password'
    database = 'inggeosoftmysql'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or  \
        'mysql+pymysql://root:pass@localhost/flask_app_db'
    


class ProdnConfig(appConfig):
    DEBUG = False
    PORT = 5000

    server = 'localhost'
    username = 'root'
    password = 'password'
    database = 'inggeosoftmysql'

    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or  \
        'mysql+pymysql://root:pass@localhost/flask_app_db'




"""Flask configuration variables."""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False