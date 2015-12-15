# -*- coding: utf-8 -*-
# !/usr/bin/env python
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__, instance_relative_config=True)
# Load the default configuration
app.config.from_object('config.default')
app.config.from_pyfile('config.py')
# Load the file specified by the APP_CONFIG_FILE environment variable
# app.config.from_envvar('config.')
db = SQLAlchemy(app)
from app import views, models


# start.sh

# APP_CONFIG_FILE=/var/www/yourapp/config/production.py
# python run.py
