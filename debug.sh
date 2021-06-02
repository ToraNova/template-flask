#!/bin/sh

# runs the flask project with gunicorn, please ensure in virtualenv!
# on localhost port 4000 with 4 worker threads.
gunicorn -w 4 -b 127.0.0.1:4000 "project_name:create_app()"

# if using eventlet (socketio)
#gunicorn --worker-class eventlet -w 1 -b 127.0.0.1:5000 "ocrweb:create_app()"
