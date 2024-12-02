from models import Question
from extensions import db

def test_question(client):
    # Configurar el contexto de la aplicación y añadir una pregunta específica
    with client.application.app_context():
        # Elimina cualquier pregunta existente en la base de datos para evitar conflictos
        Question.query.delete()
        db.session.commit()

        # Añadir una nueva pregunta específica para este test
        question = Question(
            category='Ciencia',
            text='Cual es la formula quimica del agua?',
            options="['H2O', 'CO2', 'O2', 'H2']",
            correct_answer='H2O'
        )
        db.session.add(question)
        db.session.commit()

    # Configurar la sesión para la categoría seleccionada
    with client.session_transaction() as session:
        session['selected_category'] = 'Ciencia'
        session['answered_questions'] = []

    # Realizar la solicitud GET al endpoint
    response = client.get('/question')

    # Verificar que la respuesta es correcta
    assert response.status_code == 200
    assert b'Pregunta' in response.data
    assert b'Cual es la formula quimica del agua?' in response.data
