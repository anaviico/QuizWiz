from models import Question
from extensions import db
from app import app


def test_questions_existence(client):
    """Comprueba que existen preguntas en la base de datos y que se pueden recuperar."""
    with client.application.app_context():
        questions = Question.query.all()

        assert len(questions) > 0, "No hay preguntas en la base de datos"

    response = client.get('/question')

    assert response.status_code == 200, "El endpoint no responde correctamente"
    assert b'Pregunta' in response.data, "La respuesta no contiene el encabezado esperado de 'Pregunta'"
