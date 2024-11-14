import sys
sys.path.append('QuizWiz-Backend')  # Agrega la ruta de tu módulo al path
from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test para verificar que la página de inicio carga correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data
