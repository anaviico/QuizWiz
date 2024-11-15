def test_submit_answer(client):
    with client.session_transaction() as session:
        session['selected_category'] = 'Geografía'
        session['answered_questions'] = []
        session['correct_answers'] = 0

    response = client.post('/submit_answer', data={'question_id': 1, 'answer': 'H2O'})
    assert response.status_code == 302  

    with client.session_transaction() as session:
        print("Correct Answers in Session después de la redirección:", session['correct_answers'])

    assert session['correct_answers'] == 1 