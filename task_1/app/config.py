import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
WTF_CSRF_ENABLED = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

STANDART_PAGE_COUNT = 20
