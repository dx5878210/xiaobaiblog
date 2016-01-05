# -*- coding: utf-8 -*-
# !/usr/bin/env python
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask import Flask
from config.default import basedir


app = Flask(__name__, instance_relative_config=True)
# Load the default configuration
app.config.from_object('config.default')
#app.config.from_pyfile('config.py')
# Load the file specified by the APP_CONFIG_FILE environment variable
# app.config.from_envvar('config.')


# db config
db = SQLAlchemy(app)

# user-login config
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))
from app import views, models


# start.sh

# APP_CONFIG_FILE=/var/www/yourapp/config/production.py
# python run.py
