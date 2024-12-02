# Hito 3: Diseño de Microservicios

## 🎯 Introducción y Objetivos

En este hito, se ha avanzado en el desarrollo de **QuizWiz** al convertir el backend en un microservicio con una API clara. Esto incluye:

- Crear rutas para manejar las interacciones de los usuarios.
- Desacoplar la lógica de negocio de las rutas de la API.
- Añadir un sistema de logs para monitorizar el funcionamiento de la app.
- Implementar pruebas unitarias y funcionales para garantizar la estabilidad del microservicio.



## 🖥️ 1. Diseño de la API

### 🌐 1.1 Rutas Principales

El diseño de la API se basó en un esquema RESTful, con las siguientes rutas:

- **GET `/`**: Página de inicio que muestra las categorías disponibles.
- **GET `/category`**: Selección de una categoría y configuración de la sesión.
- **GET `/question`**: Devuelve una pregunta no respondida de la categoría seleccionada.
- **POST `/submit_answer`**: Valida la respuesta del usuario.
- **GET `/results`**: Muestra los resultados.

#### Ejemplo de implementación:
```python
from flask import Blueprint, request, session, redirect, url_for
from services import get_categories, get_unanswered_questions, check_answer, calculate_results
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

La estructura del proyecto se ha organizado de la siguiente manera:

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
- **test/**: Ficheros que incluyen las pruebas.



### 🧑‍💻 Beneficios del Diseño por Capas

La separación entre rutas, lógica de negocio y modelos facilita:

- **Mantenibilidad**: Los cambios en una capa no afectan totalmente a las demás.
- **Pruebas**: Permite probar la lógica de negocio de forma independiente.
- **Escalabilidad**: Se puede añadir nueva funcionalidad sin modificar el código anterior.



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
2024-11-27 16:34:29,993 - INFO - Categoría seleccionada: Historia
2024-11-27 16:34:30,010 - INFO - 127.0.0.1 - - [02/Dec/2024 16:34:30] "GET /question HTTP/1.1" 200 -
```

### 📋 Justificación del Sistema de Logs

El sistema de logs se realizó utilizando el módulo `logging` de Python por:

- **Simplicidad**: Es una solución ligera y fácil.
- **Flexibilidad**: Permite registrar información personalizada en diferentes niveles (INFO, ERROR, etc.).
- **Compatibilidad**: No requiere dependencias externas.


## 🧪 3. Pruebas Unitarias y Funcionales

Se han implementado más pruebas con **pytest** para validar la API y la lógica de negocio. 

### 🌐 3.1 Pruebas de Endpoints

#### **Prueba de la página de inicio**
```python
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data
    assert b'Historia' in response.data  
```

```
(venv) PS C:\Users\analu\Desktop\INFORMATICA\Master\PRIMERCUATRI\CC2\QuizWiz> pytest 
=============================== test session starts ================================
platform win32 -- Python 3.9.13, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\analu\Desktop\INFORMATICA\Master\PRIMERCUATRI\CC2\QuizWiz
configfile: pytest.ini
testpaths: test
plugins: flask-1.3.0
collected 5 items

test\test_app.py .                                                            [ 20%]
test\test_category.py .                                                       [ 40%] 
test\test_questions.py .                                                      [ 60%]
test\test_results.py .                                                        [ 80%] 
test\test_submit_answerd.py .                                                 [100%]

================================ 5 passed in 0.16s ================================= 
```

### 🤖 Ejecución de Pruebas en GitHub Actions

El pipeline de CI de **GitHub Actions** se configuró para ejecutar estas pruebas automáticamente cada vez que se realiza un `push` o `pull request` en la rama `main`. Esta automatización permite que los errores se detecten pronto y que la calidad del código se mantenga sin esfuerzo.



## ✅ Conclusión

El diseño del microservicio para **QuizWiz** cumple con los objetivos, incluyendo:

- Un API RESTful funcional y desacoplada.
- Sistema de logs para monitorizar la actividad.
- Pruebas automatizadas para asegurar la calidad del proyecto.

Las pruebas realizadas tanto localmente como en el pipeline de CI confirman que la app responde correctamente en distintos escenarios, garantizando estabilidad y escalabilidad para futuras mejoras.