__author__ = 'bogdan'


import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')

THEME = 'default'

SECRET_KEY = 'ofhAOU4HT28998IUHPGWbrgkjkj)()*&&&&'
DEBUG = True