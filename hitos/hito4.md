# Hito 4: Composición de Servicios con Docker Compose

## 🎯 Introducción y Objetivos

En este hito, **QuizWiz** ha evolucionado hacia una infraestructura basada en **contenedores** utilizando **Docker y Docker Compose**. Esto permite una mayor **portabilidad, escalabilidad y reproducibilidad** del entorno de desarrollo y despliegue.

Los objetivos principales de este hito fueron:

- Contenerizar la aplicación y la base de datos PostgreSQL en **Docker**.
- Utilizar **Docker Compose** para gestionar múltiples contenedores en un **clúster**.
- Configurar un entorno de pruebas para ejecutar la aplicación en contenedores.
- Asegurar la correcta integración con **GitHub Actions** para pruebas automatizadas.
- Subir el contenedor de la aplicación a **GitHub Packages** y configurar su actualización automática.

---

## 🏠 1. Contenerización de la Aplicación

### 📦 1.1 Creación del Dockerfile

Para contenerizar la aplicación, se creó un `Dockerfile` basado en **Python 3.10-slim** que instala las dependencias y expone la aplicación:

```dockerfile
# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . /app

# Exponer el puerto que usa Flask (5000)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
```

### 🔗 1.2 Creación de `docker-compose.yml`

Para gestionar la aplicación y la base de datos PostgreSQL, se utilizó **Docker Compose** con la siguiente configuración:

```yaml
version: "3.9"
services:
  app:
    build:
      context: ./QuizWiz_Backend
      dockerfile: Dockerfile
    container_name: quizwiz-app
    ports:
      - "8000:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://postgres:root@db:5432/quizwiz
    depends_on:
      - db
  db:
    image: postgres:15
    container_name: quizwiz-db
    ports:
      - "5433:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: root
      POSTGRES_DB: quizwiz
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

#### 📌 **Explicación de los servicios**
- **`db`**: Contenedor con PostgreSQL que almacena los datos.
- **`app`**: Contenedor que ejecuta la aplicación Flask y se conecta a la base de datos.
- **`volumes`**: Se utiliza `pgdata` para persistencia de datos en la base de datos.

---

## ⚙️ 2. Configuración de la Base de Datos en Docker

Al ejecutar los contenedores con `docker-compose up`, se requiere que la base de datos tenga las tablas correctamente creadas. Para esto, se utilizó un script de inicialización (`init_db.py`):

```python
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
```

Este script se ejecuta al iniciar los contenedores para asegurarse de que la base de datos tiene la estructura correcta antes de realizar cualquier prueba.

---

## 🤖 3. Pruebas Automatizadas con Docker

### 🔄 3.1 Ejecución de Pruebas con `pytest`

Se realizaron pruebas automatizadas para validar el correcto funcionamiento de la aplicación dentro de los contenedores. 

```bash
docker-compose run app pytest
```

### 🌐 3.2 Pruebas de Integración en GitHub Actions

Para garantizar que la infraestructura basada en contenedores funcione correctamente en cada actualización del código, se configuró un pipeline de **GitHub Actions**. 

El flujo de trabajo realiza los siguientes pasos:
1. **Levantar los contenedores** con la aplicación y la base de datos PostgreSQL en un entorno controlado.
2. **Ejecutar la inicialización de la base de datos**, asegurando que la estructura de las tablas está correctamente creada.
3. **Lanzar las pruebas automatizadas con `pytest`** dentro del contenedor de la aplicación.
4. **Verificar el estado de la ejecución**, reportando los errores en caso de fallo.

Este pipeline se activa automáticamente con cada `push` o `pull request` a la rama `main`, proporcionando una validación continua del funcionamiento del sistema.

---

## ✅ Conclusión

El uso de **Docker y Docker Compose** en **QuizWiz** ha permitido:

- **Estandarizar el entorno** de desarrollo y despliegue.
- **Facilitar la gestión de dependencias** con PostgreSQL y la aplicación en contenedores.
- **Automatizar pruebas** dentro del entorno de CI/CD con GitHub Actions.
- **Garantizar la reproducibilidad** del sistema en diferentes entornos.

Con esta configuración, **QuizWiz** ahora está preparado para un despliegue más robusto y escalable. 🚀
