from QuizWiz_Backend.models import Question
from QuizWiz_Backend.extensions import db

def test_choose_category(client):
    with client.session_transaction() as session:
        session['selected_category'] = None
        session['answered_questions'] = []
    
    response = client.get('/category?category=Historia')
    assert response.status_code == 302  # Redirección
    assert '/question' in response.headers['Location']  # Verifica redirección a /question

    # Verificar que la categoría se guarda correctamente en la sesión
    with client.session_transaction() as session:
        assert session['selected_category'] == 'Historia'