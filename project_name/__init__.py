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

from project_name import extra, bpex, middleware

import datetime

def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True, )
    # warning: please set a fixed string if using multi-workers
    # the following only works with worker count = 1
    app.secret_key = secrets.token_urlsafe(32)
    app.testing = False

    if test_config:
        # to use a test_config, do create_app({"TESTING":True}), test_config is a dict
        app.config.from_mapping(test_config)

    @app.route('/redir')
    def redir():
        return redirect(url_for('hello'))

    @app.route('/')
    def root():
        return 'go to hello?'

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        d = datetime.datetime.now()
        return render_template('hello.html', data = d)

    extra.init_app(app) # initialize routes not defined here
    app.register_blueprint(bpex.bp)

    app.wsgi_app = middleware.PathPrefix(app.wsgi_app, prefix='/project')

    return app
