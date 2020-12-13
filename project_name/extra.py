'''
sample of defining routes outside of __init__.py file
'''

from flask import url_for

def init_app(app):

    @app.route('/extra/<dpath>')
    def extra(dpath):
        return 'welcome to extra stuffs %s. checkout blueprints %s' % (dpath, url_for('bpex.sample'))

    return app
