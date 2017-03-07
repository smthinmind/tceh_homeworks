
__author__ = 'dkorney'

DEBUG = True
SECRET_KEY = 'My secret key'

# Database settings:
SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False
