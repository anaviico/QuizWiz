
def test_question_page(client):
    """Test para verificar que la página de preguntas carga correctamente"""
    response = client.get('/question')
    assert response.status_code == 200
    assert b'Pregunta' in response.data  