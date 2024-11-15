# Hito 2: Integración continua

## 1. Introducción y Objetivos

El desarrollo de aplicaciones web modernas requiere no solo la implementación de funcionalidades robustas, sino también la capacidad de asegurar su correcto funcionamiento a través de pruebas y sistemas de integración continua. Este proyecto se centra en la implementación de un sistema de pruebas y la configuración de un pipeline de CI/CD para **QuizWiz**, una aplicación de preguntas y respuestas. Los objetivos principales son:

- Desarrollar pruebas que aseguren la calidad del código y la funcionalidad de la aplicación.
- Implementar un pipeline de integración continua que permita la ejecución automática de pruebas.
- Justificar y documentar la elección de herramientas y métodos utilizados.

## 2. Descripción General de la Aplicación

**QuizWiz** es una aplicación de preguntas y respuestas que permite a los usuarios seleccionar una categoría, responder preguntas y ver sus resultados al final. La aplicación está diseñada para proporcionar una experiencia de juego sencilla e interactiva. Las funcionalidades son:

- **Selección de categoría**
- **Respuestas y evaluación**

## 3. Elección y uso del marco de pruebas (1.5 puntos)

Para asegurar la calidad del código y la funcionalidad de **QuizWiz**, se decidió utilizar **pytest** como marco de pruebas. Esta elección se basa en los siguientes puntos:

- **Simplicidad y claridad**: Posee una sintaxis sencilla y capacidad de escribir pruebas de forma clara y concisa.
- **Flexibilidad**: Permite la creación de fixtures reutilizables, facilitando la configuración del entorno de pruebas.
- **Extensibilidad**: Cuenta con una gran variedad de plugins que amplían sus capacidades, como `pytest-flask`.

### Ejemplo de implementación de pruebas con **pytest**:
Se han creado pruebas para la funcionalidad de carga de la página de inicio y la visualización de categorías. Una de las pruebas implementadas es la siguiente:

```python
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenido a QuizWiz' in response.data  
```

Esta prueba comprueba que la página de inicio se cargua correctamente y que tiene el texto "Bienvenido a QuizWiz".

