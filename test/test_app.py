from QuizWiz_Backend.app import app
from QuizWiz_Backend.extensions import db

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data