from app import app
from extensions import db
from models import Question

def test_submit_answer(client):
    with client.application.app_context():
        question = Question(
            category='Geografía',
            text='¿Cuál es la capital de Francia?',
            options="['París', 'Londres', 'Roma', 'Berlín']",
            correct_answer='París'
        )
        db.session.add(question)
        db.session.commit()

    with client.session_transaction() as session:
        session['selected_category'] = 'Geografía'
        session['answered_questions'] = []
        session['correct_answers'] = 0

    response = client.post(
        '/submit_answer',
        data={'question_id': 1, 'answer': 'París'}
    )

    assert response.status_code == 302  # Redirección tras enviar respuesta
    assert response.headers['Location'].endswith('/question')  # Redirige correctamente
