import os

basedir = os.path.abspath(os.path.dirname(__file__))
CONTOUR = os.environ.get('contour', 'testing')
if CONTOUR == 'testing':
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'SECRET'

STANDART_PAGE_COUNT = 20
