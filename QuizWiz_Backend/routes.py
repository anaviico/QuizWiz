from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from services import get_categories, get_unanswered_questions, check_answer, calculate_results
import random
from logging_config import logger

bp = Blueprint('quiz', __name__)

@bp.route('/', methods=['GET'])
def home():
    """Ruta para la página principal: muestra las categorías."""
    categories = get_categories()
    return render_template('index.html', categories=categories)

@bp.route('/category', methods=['GET'])
def choose_category():
    selected_category = request.args.get('category')
    session['selected_category'] = selected_category
    session['answered_questions'] = [] 
    session['correct_answers'] = 0  
    logger.info(f"Categoría seleccionada: {selected_category}")  # Log aquí
    return redirect(url_for('quiz.get_question'))

@bp.route('/question', methods=['GET'])
def get_question():
    """Ruta para obtener una pregunta no respondida."""
    if 'selected_category' not in session:
        flash('Por favor, selecciona una categoría para comenzar.')
        return redirect(url_for('quiz.home'))

    category = session['selected_category']

    if len(session['answered_questions']) >= 10:
        flash('Has respondido todas las preguntas de esta partida.')
        return redirect(url_for('quiz.show_results'))

    unanswered_questions = get_unanswered_questions(category, session['answered_questions'])

    if not unanswered_questions:  # Si no hay preguntas no respondidas
        flash('No quedan más preguntas en esta categoría.')
        return redirect(url_for('quiz.show_results'))

    question = random.choice(unanswered_questions)

    question_data = {
        "id": question.id,
        "text": question.text,
        "options": question.options,  
        "category": question.category
    }
    current_question_number = len(session['answered_questions']) + 1
    total_questions = 10

    return render_template(
        'question.html',
        question=question_data,
        current_question_number=current_question_number,
        total_questions=total_questions
    )

@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    """Ruta para enviar una respuesta y verificarla."""
    question_id = int(request.form.get('question_id'))
    user_answer = request.form.get('answer')

    question = next(
        (q for q in get_unanswered_questions(session['selected_category'], session['answered_questions'])
         if q.id == question_id), 
        None
    )

    if question is None:
        flash('Pregunta no encontrada.')
        return redirect(url_for('quiz.get_question'))

    if question_id not in session['answered_questions']:
        session['answered_questions'].append(question_id)
        session.modified = True  

    if question.correct_answer.lower() == user_answer.lower():
        flash('¡Respuesta correcta!')
        session['correct_answers'] = session.get('correct_answers', 0) + 1
    else:
        flash('Respuesta incorrecta. Inténtalo de nuevo.')

    return redirect(url_for('quiz.get_question'))

@bp.route('/results', methods=['GET'])
def show_results():
    """Ruta para mostrar los resultados."""
    total_questions = len(session.get('answered_questions', []))
    correct_answers = session.get('correct_answers', 0)

    return render_template(
        'result.html',
        total_questions=total_questions,
        correct_answers=correct_answers
    )
