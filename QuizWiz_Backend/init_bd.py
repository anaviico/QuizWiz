from app import app
from extensions import db
from models import Question

with app.app_context():
    db.create_all()

    # Inserta datos iniciales para evitar fallos en los tests
    question = Question(
        category="General",
        text="¿Cuál es la capital de España?",
        correct_answer="Madrid",
        options=["Madrid", "Barcelona", "Valencia", "Sevilla"]
    )
    db.session.add(question)
    db.session.commit()
