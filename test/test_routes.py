import pytest

def test_question_page(client):
    response = client.get('/question')
    assert response.status_code == 200