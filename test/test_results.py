def test_results(client):
    with client.session_transaction() as session:
        session['selected_category'] = 'Historia'
        session['correct_answers'] = 3
        session['answered_questions'] = [1, 2, 3, 4, 5]

    response = client.get('/results')
    assert response.status_code == 200
    assert '<h1>¡Test Completado!</h1>'.encode('utf-8') in response.data
    assert 'Has respondido correctamente <strong>3</strong> de <strong>5</strong> preguntas.'.encode('utf-8') in response.data
