import os
from app import app
from extensions import db
from models import Question
from config import TestingConfig

if os.getenv("FLASK_ENV") == "testing":
    app.config.from_object(TestingConfig)

with app.app_context():
    db.create_all()

    question = Question(
        category="General",
        text="¿Cuál es la capital de España?",
        correct_answer="Madrid",
        options=["Madrid", "Barcelona", "Valencia", "Sevilla"]
    )
    db.session.add(question)
    db.session.commit()
