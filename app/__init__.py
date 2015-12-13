# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config.from_object("config")
db=SQLAlchemy(app)
from app import views, models
