from examples import sample

def test_config():
    """Test create_app without passing test config."""
    assert not sample.create_app().testing
    assert sample.create_app({"TESTING": True}).testing
