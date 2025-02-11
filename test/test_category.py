from models import Question
from extensions import db

def test_choose_category(client):
    with client.session_transaction() as session:
        session['selected_category'] = None
        session['answered_questions'] = []
    
    response = client.get('/category?category=Historia')
    assert response.status_code == 302  
    assert '/question' in response.headers['Location'] 

    with client.session_transaction() as session:
        assert session['selected_category'] == 'Historia'