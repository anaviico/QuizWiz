from extensions import db
from models import Question
from app import app

# Inicializar la base de datos y agregar preguntas
with app.app_context():
    # Crear las tablas en la base de datos
    db.create_all()

    # Definir las preguntas
    questions = [
        # Categoría: Ciencia
        Question(
            category='Ciencia',
            text='¿Cuál es el símbolo químico del agua?',
            correct_answer='H2O',
            options=['H2O', 'CO2', 'O2', 'N2']
        ),
        Question(
            category='Ciencia',
            text='¿Qué planeta es conocido como el Planeta Rojo?',
            correct_answer='Marte',
            options=['Tierra', 'Marte', 'Júpiter', 'Saturno']
        ),
        Question(
            category='Ciencia',
            text='¿Cuál es la velocidad de la luz en el vacío?',
            correct_answer='299,792 km/s',
            options=['299,792 km/s', '150,000 km/s', '1,000 km/s', '3,000 km/s']
        ),
        Question(
            category='Ciencia',
            text='¿Qué gas absorben las plantas de la atmósfera?',
            correct_answer='Dióxido de Carbono',
            options=['Dióxido de Carbono', 'Oxígeno', 'Nitrógeno', 'Hidrógeno']
        ),
        Question(
            category='Ciencia',
            text='¿Cuál es la "fábrica de energía" de la célula?',
            correct_answer='Mitocondria',
            options=['Mitocondria', 'Núcleo', 'Ribosoma', 'Aparato de Golgi']
        ),

        # Categoría: Historia
        Question(
            category='Historia',
            text='¿Quién fue el primer presidente de los Estados Unidos?',
            correct_answer='George Washington',
            options=['George Washington', 'Abraham Lincoln', 'John Adams', 'Thomas Jefferson']
        ),
        Question(
            category='Historia',
            text='¿En qué año se hundió el Titanic?',
            correct_answer='1912',
            options=['1912', '1905', '1918', '1920']
        ),
        Question(
            category='Historia',
            text='¿Qué civilización antigua construyó las pirámides?',
            correct_answer='Egipcios',
            options=['Egipcios', 'Romanos', 'Griegos', 'Mayas']
        ),
        Question(
            category='Historia',
            text='¿Quién fue conocida como la Dama de Hierro?',
            correct_answer='Margaret Thatcher',
            options=['Margaret Thatcher', 'Angela Merkel', 'Reina Victoria', 'Juana de Arco']
        ),
        Question(
            category='Historia',
            text='¿Qué guerra se libró entre el Norte y el Sur de los Estados Unidos?',
            correct_answer='La Guerra Civil',
            options=['La Guerra Civil', 'Primera Guerra Mundial', 'Guerra de Independencia', 'Guerra de Vietnam']
        ),

        # Categoría: Geografía
        Question(
            category='Geografía',
            text='¿Cuál es la capital de Francia?',
            correct_answer='París',
            options=['París', 'Londres', 'Berlín', 'Madrid']
        ),
        Question(
            category='Geografía',
            text='¿Cuál es el continente más grande?',
            correct_answer='Asia',
            options=['Asia', 'África', 'Europa', 'Antártida']
        ),
        Question(
            category='Geografía',
            text='¿Qué país tiene más habitantes?',
            correct_answer='China',
            options=['China', 'India', 'Estados Unidos', 'Rusia']
        ),
        Question(
            category='Geografía',
            text='¿Qué río es el más largo del mundo?',
            correct_answer='Nilo',
            options=['Nilo', 'Amazonas', 'Yangtsé', 'Misisipi']
        ),
        Question(
            category='Geografía',
            text='¿Qué desierto es el más grande del mundo?',
            correct_answer='Sáhara',
            options=['Sáhara', 'Gobi', 'Kalahari', 'Ártico']
        ),

        # Categoría: Deportes
        Question(
            category='Deportes',
            text='¿Cuántos jugadores tiene un equipo de fútbol?',
            correct_answer='11',
            options=['11', '9', '10', '12']
        ),
        Question(
            category='Deportes',
            text='¿Qué deporte es conocido como "el rey de los deportes"?',
            correct_answer='Fútbol',
            options=['Fútbol', 'Baloncesto', 'Tenis', 'Críquet']
        ),
        Question(
            category='Deportes',
            text='¿Cuál es la puntuación máxima en bolos?',
            correct_answer='300',
            options=['300', '250', '200', '150']
        ),
        Question(
            category='Deportes',
            text='¿En qué país se inventaron los Juegos Olímpicos?',
            correct_answer='Grecia',
            options=['Grecia', 'Italia', 'Estados Unidos', 'China']
        ),
        Question(
            category='Deportes',
            text='¿Cómo se llama el término para un puntaje de cero en tenis?',
            correct_answer='Love',
            options=['Love', 'Cero', 'Nada', 'Punto Nulo']
        )
    ]

    # Insertar las preguntas en la base de datos
    db.session.add_all(questions)
    db.session.commit()

    print("¡Base de datos inicializada!")
