# -*- coding: utf-8 -*-
#!/usr/bin/env python
from app import app
from app.forms import LoginForm
from flask import render_template, redirect
from flask import flash, url_for

import config


@app.route('/')
def index():
    return render_template('index.html', title='Welcome')


# @app.route('login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flask.flash('Logged in successfully')
#         next = flask.request.args.get('next')
#         if not next_is_valid(next):
#             return flask.abort(400)
#
#         return redirect(next or url_for('index'))
#     return render_template('login.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
              '",remember_me=' + str(form.remember_me.data))
        return redirect('/')
    return render_template(
        'login.html',
        title='sign in',
        form=form,
        providers=app.config['OPENID_PROVIDERS'])
