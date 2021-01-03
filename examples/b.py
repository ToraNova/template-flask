import os
import tempfile
import pytest

from examples import sample

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    db_fd, db_file = tempfile.mkstemp()
    db_uri = 'sqlite:///%s' % db_file
    app = sample.create_app({"TESTING": True, "DBURI": db_uri})

    # create the database and load test data
    with app.app_context():
        pass
    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_file)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_b(client):

    rv = client.get('/project/')
    assert rv.status_code == 200

    #rv = client.post('/login', data=dict(username="tester", password="test"), follow_redirects=True)
    #assert rv.status_code == 200
    # or 302?
