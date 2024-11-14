from flask import Blueprint, request, render_template, redirect, url_for, jsonify, flash, session
from models import db, Question
import random

bp = Blueprint('quiz', __name__)

@bp.route('/', methods=['GET'])
def home():
    # Obtener las categorías únicas de la bd
    categories = db.session.query(Question.category).distinct().all()
    categories = [category[0] for category in categories]  
    return render_template('index.html', categories=categories)

@bp.route('/category', methods=['GET'])
def choose_category():
    selected_category = request.args.get('category')
    session['selected_category'] = selected_category
    session['answered_questions'] = [] 
    session['correct_answers'] = 0  
    return redirect(url_for('quiz.get_question'))

@bp.route('/question', methods=['GET'])
def get_question():
    # Verificar si hay una categoría seleccionada
    if 'selected_category' not in session:
        flash('Por favor, selecciona una categoría para comenzar.')
        return redirect(url_for('quiz.home'))

    category = session['selected_category']
    if 'answered_questions' not in session:
        session['answered_questions'] = []

    # Filtrar preguntas por la categoría seleccionada y que no hayan sido respondidas
    unanswered_questions = Question.query.filter(
        Question.category == category,
        ~Question.id.in_(session['answered_questions'])
    ).all()

    if not unanswered_questions:
        return redirect(url_for('quiz.show_results'))

    question = random.choice(unanswered_questions)

    current_question_number = len(session['answered_questions']) + 1
    total_questions = len(Question.query.filter(Question.category == category).all())

    return render_template('question.html', question=question, current_question_number=current_question_number,
                           total_questions=total_questions)

@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    question_id = int(request.form.get('question_id'))
    user_answer = request.form.get('answer')

    question = Question.query.get(question_id)
    if question is None:
        flash('Pregunta no encontrada')
        return redirect(url_for('quiz.get_question'))

    if question_id not in session['answered_questions']:
        session['answered_questions'].append(question_id)
        session.modified = True 

    if question.correct_answer == user_answer:
        flash('¡Respuesta correcta!')
        session['correct_answers'] += 1  
    else:
        flash('Respuesta incorrecta. Inténtalo de nuevo.')

    return redirect(url_for('quiz.get_question'))

@bp.route('/results', methods=['GET'])
def show_results():
    total_questions = len(session['answered_questions'])
    correct_answers = session.get('correct_answers', 0)
    return render_template('result.html', total_questions=total_questions, correct_answers=correct_answers)