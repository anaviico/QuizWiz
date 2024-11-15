def test_question(client):
    with client.session_transaction() as session:
        session['selected_category'] = 'Geografía' 
        session['answered_questions'] = [] 

    response = client.get('/question')

    if response.status_code == 302:
        print("Redirigido a:", response.headers.get('Location'))

    assert response.status_code == 200
    assert b'Pregunta' in response.data  
