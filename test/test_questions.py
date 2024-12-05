from QuizWiz_Backend.models import Question
from QuizWiz_Backend.extensions import db
from QuizWiz_Backend.app import app


def test_questions_existence(client):
    """Comprueba que existen preguntas en la base de datos y que se pueden recuperar."""
    with client.application.app_context():
        questions = Question.query.all()

        assert len(questions) > 0, "No hay preguntas en la base de datos"

        for question in questions:
            assert question.category is not None, "La pregunta no tiene categoría"
            assert question.text is not None, "La pregunta no tiene texto"
            assert question.correct_answer is not None, "La pregunta no tiene respuesta correcta"
            assert question.options is not None, "La pregunta no tiene opciones"

    with client.session_transaction() as session:
        session['selected_category'] = questions[0].category  # Seleccionar una categoría existente
        session['answered_questions'] = []

    response = client.get('/question')

    assert response.status_code == 200, "El endpoint no responde correctamente"
    assert b'Pregunta' in response.data, "La respuesta no contiene el encabezado esperado de 'Pregunta'"
