import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get("/")
    assert rv.data == b"Hello, CI/CD with Flask and Docker!"
    assert rv.status_code == 200
