import pytest
from flask import Flask
from flask.testing import FlaskClient

from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'