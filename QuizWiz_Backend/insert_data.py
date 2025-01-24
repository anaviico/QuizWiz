from extensions import db
from app import app
from models import Question

questions = [
    # Ciencia
    {"category": "Ciencia", "text": "Cual es la formula quimica del agua?", "correct_answer": "H2O",
     "options": ["H2O", "CO2", "O2", "H2"]},
    {"category": "Ciencia", "text": "Que particula tiene carga negativa?", "correct_answer": "Electron",
     "options": ["Electron", "Proton", "Neutron", "Quark"]},
    {"category": "Ciencia", "text": "Que planeta es conocido como el planeta rojo?", "correct_answer": "Marte",
     "options": ["Marte", "Venus", "Jupiter", "Saturno"]},
    {"category": "Ciencia", "text": "Cual es el organo mas grande del cuerpo humano?", "correct_answer": "Piel",
     "options": ["Piel", "Corazon", "Higado", "Cerebro"]},
    {"category": "Ciencia", "text": "Que elemento es necesario para la fotosintesis?", "correct_answer": "Luz solar",
     "options": ["Luz solar", "Agua", "Savia", "Nitrogeno"]},
    {"category": "Ciencia", "text": "Que gas constituye la mayor parte de la atmosfera?", "correct_answer": "Nitrogeno",
     "options": ["Nitrogeno", "Oxigeno", "CO2", "Hidrogeno"]},
    {"category": "Ciencia", "text": "Cual es la distancia promedio entre la Tierra y el Sol?", "correct_answer": "150 millones",
     "options": ["150 millones", "100 millones", "200 millones", "250 millones"]},
    {"category": "Ciencia", "text": "Que tipo de sangre es conocido como donante universal?", "correct_answer": "O-",
     "options": ["O-", "O+", "A-", "AB+"]},
    {"category": "Ciencia", "text": "Que organo filtra la sangre?", "correct_answer": "Rinon",
     "options": ["Rinon", "Higado", "Corazon", "Pulmones"]},
    {"category": "Ciencia", "text": "Que animal puede cambiar de color para camuflarse?", "correct_answer": "Camaleon",
     "options": ["Camaleon", "Serpiente", "Aguila", "Leopardo"]},
    
    
    # Añade más preguntas aquí siguiendo el formato
]

with app.app_context():
    try:
        for q in questions:
            new_question = Question(
                category=q["category"],
                text=q["text"],
                correct_answer=q["correct_answer"],
                options=q["options"]
            )
            db.session.add(new_question)
        db.session.commit()
        print("Datos insertados correctamente.")
    except Exception as e:
        db.session.rollback()
        print(f"Error al insertar los datos: {e}")



