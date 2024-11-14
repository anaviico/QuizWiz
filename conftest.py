import pytest
from app import app as flask_app
import sys
sys.path.insert(0, './QuizWiz-Backend')

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client