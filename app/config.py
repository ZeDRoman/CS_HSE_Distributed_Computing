import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET'

STANDART_PAGE_COUNT = 20
