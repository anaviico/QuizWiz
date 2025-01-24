from extensions import db
from models import Question
from app import app

with app.app_context():
    questions = Question.query.all()
    for question in questions:
        print(f"ID: {question.id}, Category: {question.category}, Text: {question.text}")
