# allows prefixing entire flask project with url
# useful for multi-site servers
# see original https://stackoverflow.com/questions/18967441/add-a-prefix-to-all-flask-routes/36033627#36033627

class PathPrefix(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["not found.".encode()]
