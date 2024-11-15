# Hito 2: Integración Continua

## 🎯 Introducción y Objetivos

En el desarrollo de aplicaciones web modernas, no basta con solo programar funciones geniales. Necesitamos estar seguros de que todo funciona bien, y ahí es donde entran en juego las pruebas y la integración continua (CI).

La app está pensada para ser simple y divertida, dándole a los jugadores una experiencia fluida.

## 🖥️ 1. Creación del Backend

### ⚙️ 1.1 Instalación del Entorno de Desarrollo

Para iniciar el desarrollo de **QuizWiz**, instalé Python y configuré un entorno virtual:

```bash
python --version  # Verificar versión de Python
pip install virtualenv  # Instalar virtualenv
python -m venv env  # Crear entorno virtual
source env/bin/activate  # Activar entorno en Linux/Mac
.\env\Scripts\activate  # Activar entorno en Windows
```

### 📦 1.2 Instalación de Dependencias

Se utilizaron **Flask** y **psycopg2** para la conexión con **PostgreSQL**. Las dependencias se instalaron y se incluyeron en `requirements.txt`:

```bash
pip install flask psycopg2-binary
pip freeze > requirements.txt 
```
En requirements.txt estan todas las dependencias, con sus versiones que son comppatibles entre si, guardadas.

### 🗂️ 1.3 Estructura del Proyecto

La estructura inicial del proyecto backend se organizó de la siguiente manera:

```
QuizWiz-Backend/
|-- app.py
|-- models.py
|-- routes.py
|-- templates/
|-- static/
|-- config.py
```

- **app.py**: Archivo principal que inicia la aplicación.
- **models.py**: Define las funciones de interacción con la base de datos.
- **routes.py**: Contiene las rutas y controladores.
- **config.py**: Configuraciones para la conexión a PostgreSQL.

### 🗄️ 1.4 Configuración de la Base de Datos

Se configuró **PostgreSQL** y se creó la base de datos \`quizwiz_db\`. La conexión en **config.py** se realizó de la siguiente manera:

```python
DATABASE_URL = "postgresql://user:password@localhost:5433/quizwiz_db"
```

### 🚀 1.5 Configuración Inicial de Flask

El archivo **app.py** inicializa la aplicación y registra las rutas:

```python
from flask import Flask
from routes import init_routes

app = Flask(__name__)
app.config.from_object('config')

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
```

## 🛤️ 2. Desarrollo de Funcionalidades y Endpoints

Se desarrollaron los endpoints para manejar las funcionalidades de la app, como seleccionar categorías, responder preguntas y mostrar resultados. Un ejemplo de un endpoint básico es:

```python
from flask import Blueprint, jsonify, request

@bp.route('/', methods=['GET'])
def home():
    categories = db.session.query(Question.category).distinct().all()
    categories = [category[0] for category in categories]  
    return render_template('index.html', categories=categories)
```
En el cual se inicia la aplicación, cargando el index.html.


## 🔧 3. Elección y Configuración del Gestor de Tareas

Se eligió **GitHub Actions** como el motor para la integración continua. ¿Por qué? Porque:

- **Integración con GitHub**: Al ser parte de la misma plataforma,a configuración es simple y directa.
- **Documentación y soporte**: Existe una gran variedad de recursos en línea, desde documentación oficial hasta tutoriales y ejemplos prácticos.
- **Flexibilidad y escalabilidad**: Permite personalizar los procesos para que se adapten exactamente a lo que necesitamos.

La configuración se hace con un archivo YAML que se guarda en el directorio `.github/workflows/`. Este archivo define los pasos que debe seguir el pipeline, como instalar dependencias y ejecutar pruebas, cada vez que alguien sube o actualiza el código en la rama `main`.

### Detallles de la configuración:

El archivo `ci.yml` para QuizWiz define el proceso de CI y asegura que las pruebas se ejecuten en cada cambio de código:

```yaml
name: CI Workflow

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:latest
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: root
          POSTGRES_DB: quizwiz
        ports:
          - 5433:5432
        options: >-
          --health-cmd "pg_isready -U postgres"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9.13'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Set FLASK_ENV to testing
        run: echo "FLASK_ENV=testing" >> $GITHUB_ENV
      - name: Set PYTHONPATH
        run: echo "PYTHONPATH=${GITHUB_WORKSPACE}/QuizWiz-Backend" >> $GITHUB_ENV
      - name: Wait for PostgreSQL to be ready
        run: |
          for i in {1..10}; do
            if pg_isready -h localhost -p 5433 -U postgres; then
              echo "PostgreSQL is ready"
              break
            fi
            echo "Waiting for PostgreSQL..."
            sleep 3
          done
      - name: Initialice database
        run: |
          python -c "
          from app import db, app
          with app.app_context():
            db.create_all()
          "
        
      - name: Run tests
        env:
          DATABASE_URL: postgres://postgres:root@localhost:5433/quizwiz
        run: pytest

```

## 🧪 4. Elección y Uso de la Biblioteca de Aserciones

Se ha utilizado **pytest** como biblioteca de aserciones porque:

- **Simplicidad y eficacia**: Las pruebas se pueden escribir y entender facilmente.
- **Compatibilidad con Flask**: Usando `pytest-flask`, se pueden probar rutas y funciones específicas de la app.
- **Ayuda a detectar errores rápidamente**: Sus reportes detallados facilitan mucho encontrar y solucionar problemas.

Esta elección hizo que se pudiesen crear unas pruebas útiles para **QuizWiz**, tanto en desarrollo local como en GitHub.

## 🛡️ 5. Elección y Uso del Marco de Pruebas

El marco de pruebas elegido fue **pytest**, que no solo se utilizó como biblioteca de aserciones, sino también como marco general para la ejecución de pruebas, y esto fue por:

- **Flexibilidad**: Permite crear pruebas tanto unitarias como integradas de manera eficiente.
- **Plugins**: Como `pytest-flask`, que expande sus funcionalidades.
- **Automatización completa del pipeline**: Se integra sin problemas con GitHub Actions, lo que permite la automatización de las pruebas.

## ✅ 6. Integración Continua Funcionando y Justificación

La implementación de la integración continua con **GitHub Actions** mejoró la calidad del proyecto y permitió la detección de errores desde el inicio. Se eligió esta herramienta porque:

- **Integración con GitHub**: Se aprovechó la estrecha integración con los repositorios de GitHub.
- **Personalización avanzada**: Los pipelines se adaptan a lo que necesita el programador.
- **Automatización**: Todo se gestiona automáticamente cada vez que se realiza un cambio en el código.

El archivo de configuración (`ci.yml`) asegura que cada cambio en la rama `main` pase por los pasos de revisión, como la instalación de dependencias y la ejecución de pruebas, sin intervención manual.

## 🔍 7. Implementación y Ejecución de Tests

Para que la app **QuizWiz** cumpla con lo que se espera de ella, se implementaron pruebas unitarias e integradas. Estas pruebas se enfocaron en garantizar que la app respondiera correctamente a las interacciones de los usuarios y en validar la lógica de manejo de las respuestas.

### 🌐 Pruebas de Endpoints
Se hicieron pruebas para confirmar que los principales endpoints de la app respondieran de forma correcta y que los datos fueran consistentes. Esto ayuda a que los usuarios interactúen con la app sin problemas y reciban respuestas adecuadas.

```python
from app import app, db

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data
```

Esta prueba verifica que el endpoint de la página de inicio devuelva un código de estado 200 y contenga el texto adecuado en la respuesta.

### 🧠 Pruebas de la Lógica de Negocio
También se probaron aspectos clave de la lógica de la app, como la obtención de una pregunta desde la base de datos y la correcta interacción con la lógica de la aplicación:

```python
from models import db, Question

def test_question(client):
    with client.application.app_context():
        question = Question(category='Geografía', text='¿Cuál es la capital de Francia?', options=['París', 'Londres', 'Roma'], correct_answer='París')
        db.session.add(question)
        db.session.commit()

    with client.session_transaction() as session:
        session['selected_category'] = 'Geografía'
        session['answered_questions'] = []

    response = client.get('/question')

    if response.status_code == 302:
        print("Redirigido a:", response.headers.get('Location'))

    assert response.status_code == 200
    assert b'Pregunta' in response.data
```
Esta prueba verifica que el endpoint de obtención de preguntas responde con éxito y que la respuesta contiene el texto "Pregunta".

### 🤖 Ejecución de Pruebas en GitHub Actions
El pipeline de CI de **GitHub Actions** se configuró para ejecutar estas pruebas automáticamente cada vez que se realiza un `push` o `pull request` en la rama `main`. Esta automatización permite que los errores se detecten pronto y que la calidad del código se mantenga sin esfuerzo.

### 📊 Resultados de las Pruebas
Las pruebas se ejecutaron tanto en local como en el entorno de CI de GitHub Actions. Los resultados fueron positivos: los endpoints respondieron como se esperaba y la lógica de negocio funcionó bien, lo que confirmó que la app estaba lista para manejar distintos escenarios de uso sin problemas.

## 📝 Conclusión
Implementar pruebas y un sistema de CI con **GitHub Actions** mejoró la calidad de **QuizWiz** y dio más confianza en el código. Las pruebas automatizadas ayudan a que el desarrollo sea más rápido y seguro, reduciendo el riesgo de errores al añadir nuevas funciones o hacer cambios.
