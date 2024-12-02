# Hito 3: Diseño de Microservicios

## 🎯 Introducción y Objetivos

En esta etapa, se ha dado el siguiente paso en el desarrollo de **QuizWiz** al convertir el backend en un microservicio con una API clara. Esto incluye:

- Crear rutas para manejar las interacciones de los usuarios.
- Desacoplar la lógica de negocio de las rutas de la API.
- Añadir un sistema de logs para monitorizar el funcionamiento de la app.
- Implementar pruebas unitarias y funcionales para garantizar la estabilidad del microservicio.

---

## 🖥️ 1. Diseño de la API

### 🌐 1.1 Rutas Principales

El diseño de la API se basó en un esquema RESTful, con las siguientes rutas:

- **GET `/`**: Página de inicio que muestra las categorías disponibles.
- **GET `/category`**: Selección de una categoría y configuración de la sesión.
- **GET `/question`**: Devuelve una pregunta no respondida de la categoría seleccionada.
- **POST `/submit_answer`**: Valida la respuesta del usuario.
- **GET `/results`**: Muestra los resultados del cuestionario.

#### Ejemplo de implementación:
```python
from flask import Blueprint, request, jsonify
from services import get_categories, get_unanswered_questions, check_answer, calculate_results
import random
from logging_config import logger

bp = Blueprint('quiz', __name__)

@bp.route('/category', methods=['GET'])
def choose_category():
    selected_category = request.args.get('category')
    session['selected_category'] = selected_category
    session['answered_questions'] = [] 
    session['correct_answers'] = 0  
    logger.info(f"Categoría seleccionada: {selected_category}") 
    return redirect(url_for('quiz.get_question'))
```

### 🧠 1.2 Lógica de Negocio

La lógica de negocio está en `services.py`. Esto permite que las rutas llamen funciones específicas en lugar de contener lógica dentro de ellas. Ejemplos:

- `get_categories()`: Devuelve las categorías de las preguntas de la base de datos.
- `get_unanswered_questions(category, answered_questions)`: Encuentra preguntas no respondidas por el usuario.
- `check_answer(question_id, user_answer)`: Verifica si la respuesta es correcta.

#### Ejemplo de implementación:
```python
def get_categories():
    """Obtiene todas las categorías disponibles de la base de datos."""
    categories = db.session.query(Question.category).distinct().all()
    return [category[0] for category in categories]
```

### 🗂️ 1.3 Estructura del Proyecto

La estructura del proyecto se ha organizado siguiendo las mejores prácticas de desacoplamiento:

```
QuizWiz-Backend/
|- templates/
|- static/
|- app.py
|- routes.py
|- services.py
|- models.py
|- config.py
|- logging_config.py
|- init_bd.py
|- extensions.py
test/
|- test_app.py
|- test_questions.py
|- test_submit_answer.py
```

- **app.py**: Configura la app, inicializa la base de datos y registra las rutas.
- **routes.py**: Define las rutas de la API.
- **services.py**: Tiene la lógica de negocio.
- **models.py**: Define el modelo `Question`.
- **test/**: Fichero que incluye las pruebas.

---

## 🔧 2. Sistema de Logs

Se configuró un sistema de logs para registrar actividad importante y errores. 

### Configuración de logs:
```python
import logging

logging.basicConfig(
    filename='quizwiz.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger()
```

### Ejemplo de registro:
```
2024-11-27 16:34:29,993 - INFO - Categor�a seleccionada: Historia
2024-11-27 16:34:29,995 - INFO - 127.0.0.1 - - [02/Dec/2024 16:34:29] "[32mGET /category?category=Historia HTTP/1.1[0m" 302 -
2024-11-27 16:34:30,010 - INFO - 127.0.0.1 - - [02/Dec/2024 16:34:30] "GET /question HTTP/1.1" 200 -
2024-11-27 16:34:30,046 - INFO - 127.0.0.1 - - [02/Dec/2024 16:34:30] "[36mGET /static/css/styles.css HTTP/1.1[0m" 304 -
2024-11-27 16:35:18,030 - INFO - 127.0.0.1 - - [02/Dec/2024 16:35:18] "GET /question HTTP/1.1" 200 -
2024-11-27 16:35:18,060 - INFO - 127.0.0.1 - - [02/Dec/2024 16:35:18] "[36mGET /static/css/styles.css HTTP/1.1[0m" 304 -

```

---

## 🧪 3. Pruebas Unitarias y Funcionales

Se han implementado pruebas con **pytest** para validar la API y la lógica de negocio. Esto asegura que los endpoints funcionan como se espera y que la lógica no tiene errores.

### 🌐 3.1 Pruebas de Endpoints

#### **Prueba de la página de inicio**
```python
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data
```


### 🔍 3.2 Resultados de las Pruebas

Las pruebas se ejecutaron localmente con `pytest` y también en GitHub Actions, confirmando que el sistema responde correctamente a distintos escenarios.

#### Ejemplo de salida:
```plaintext
pytest
========================================================================== test session starts ===========================================================================
platform win32 -- Python 3.9.13, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\analu\Desktop\INFORMATICA\Master\PRIMERCUATRI\CC2\QuizWiz
configfile: pytest.ini
testpaths: test
plugins: flask-1.3.0
collected 3 items

test\test_app.py .                                                                                                                                                  [ 33%]
test\test_questions.py .                                                                                                                                            [ 66%]
test\test_submit_answerd.py .                                                                                                                                       [100%]

=========================================================================== 3 passed in 0.17s ============================================================================ 
```

---

## ✅ Conclusión

El diseño del microservicio para **QuizWiz** cumple con los objetivos, incluyendo:
- Un API RESTful funcional y desacoplada.
- Sistema de logs para monitorizar la actividad.
- Pruebas automatizadas para asegurar la calidad del proyecto.