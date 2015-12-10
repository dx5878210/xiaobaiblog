# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app 
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html',title='Welcome')

