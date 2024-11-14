import pytest
from app import app, db

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data  # Ajusta este texto a lo que tengas en tu página de inicio
