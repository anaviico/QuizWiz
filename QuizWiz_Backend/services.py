from .models import Question
from .extensions import db

def get_categories():
    """Obtiene todas las categorías disponibles de la base de datos."""
    categories = db.session.query(Question.category).distinct().all()
    return [category[0] for category in categories]

def get_unanswered_questions(category, answered_questions):
    """Obtiene preguntas no respondidas de una categoría específica."""
    return Question.query.filter(
        Question.category == category,
        ~Question.id.in_(answered_questions)
    ).all()

def check_answer(question_id, user_answer):
    """Verifica si la respuesta del usuario es correcta."""
    question = db.session.get(Question, question_id)
    if not question:
        return None  # Si la pregunta no existe
    return question.correct_answer == user_answer

def calculate_results(answered_questions, correct_answers):
    """Calcula los resultados finales."""
    return {
        "total_questions": len(answered_questions),
        "correct_answers": correct_answers
    }
