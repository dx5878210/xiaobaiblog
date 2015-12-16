# default env
# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(basedir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Flask-WTF config
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accouts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com/accouts'}
]


DEBUG = False
SQLALCHEMY_ECHO = False
MAIL_FROM_EMAIL = 'dx5878210@gmail.com'
