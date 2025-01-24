from app import app
from extensions import db

def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data