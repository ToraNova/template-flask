# app constructor
'''
the create_app is used by 'flask' executable on export FLASK_APP
run with:
export FLASK_APP=<project_name>
export FLASK_ENV=development/(production: default)
flask run
flask run --no-reload (no reloading)
'''

import secrets
from flask import Flask, render_template, redirect, url_for

import datetime

def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True, )
    app.secret_key = secrets.token_urlsafe(32) # can be a fixed string as well
    app.testing = False

    if test_config:
        # to use a test_config, do create_app({"TESTING":True}), test_config is a dict
        app.config.from_mapping(test_config)

    @app.route('/')
    def root():
        return redirect(url_for('hello'))

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        d = datetime.datetime.now()
        return render_template('hello.html', data = d)

    return app
