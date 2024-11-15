def test_question(client):
    with client.session_transaction() as session:
        session['selected_category'] = 'Geografía'  
        session['answered_questions'] = []

    response = client.get('/question')
    assert response.status_code == 200  
