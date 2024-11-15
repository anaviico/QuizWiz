# Hito 2: Integración Continua

## Introducción y Objetivos

En el desarrollo de aplicaciones web modernas, no basta con solo programar funciones geniales. Necesitamos estar seguros de que todo funciona bien, y ahí es donde entran en juego las pruebas y la integración continua (CI).

## Descripción General de la Aplicación

**QuizWiz** es un juego interactivo en el que los usuarios pueden:

- **Elegir categorías.**
- **Responder preguntas y ver cómo les fue.**

La app está pensada para ser simple y divertida, dándole a los jugadores una experiencia fluida.

## 1. Elección y Configuración del Gestor de Tareas

Se eligió **GitHub Actions** como el motor para la integración continua. ¿Por qué? Porque:

- **Funciona de muy bien con GitHub**: Al ser parte de la misma plataforma, su configuración es muy sencilla.
- **Documentación y ejemplos**: Existen una gran variedad de ejemplos en internet, así como documentación disponible.
- **Flexibilidad**: Permite personalizar los procesos para que se adapten exactamente a lo que necesitamos.

La configuración se hace con un archivo YAML que se guarda en el directorio `.github/workflows/`. Este archivo define los pasos que debe seguir el pipeline, como instalar dependencias y ejecutar pruebas, cada vez que alguien sube o actualiza el código en la rama `main`.

## 2. Elección y Uso de la Biblioteca de Aserciones

Usamos **pytest** como biblioteca de aserciones porque:

- **Es sencilla de entender**: Las pruebas se pueden escribir y leer facilmente.
- **Funciona con Flask**: Usando `pytest-flask`, se pueden probar rutas y funciones específicas de la app.
- **Ayuda a detectar errores rápidamente**: Sus reportes detallados facilitan mucho encontrar y solucionar problemas.

## 3. Elección y Uso del Marco de Pruebas

El marco de pruebas elegido fue **pytest** por:

- **Simplicidad y practicidad**: Permite crear pruebas cortas y claras.
- **Plugins útiles**: Como `pytest-flask`, que expande sus funcionalidades.

## 4. Integración Continua Funcionando y Justificación

Implementamos la integración continua con **GitHub Actions** para mantener la calidad del proyecto. Elegimos esta herramienta porque:

- **Está integrada con GitHub**: Configurar y manejar workflows es muy sencillo.
- **Ofrece mucha personalización**: Los pipelines se adaptan a lo que necesita el programador.
- **Gran comunidad y documentación**: Siempre hay ayuda y ejemplos disponibles.

El archivo de configuración (`ci.yml`) asegura que cada cambio en la rama `main` pase por los pasos de revisión, como la instalación de dependencias y la ejecución de pruebas, sin intervención manual.

## 5. Implementación y Ejecución de Tests

Para que la app **QuizWiz** cumpla con lo que se espera de ella, se implementaron pruebas unitarias e integradas. Estas pruebas se enfocaron en garantizar que la app respondiera correctamente a las interacciones de los usuarios y en validar la lógica de manejo de las respuestas.

### Pruebas de Endpoints
Se hicieron pruebas para confirmar que los principales endpoints de la app respondieran de forma correcta y que los datos fueran consistentes. Esto ayuda a que los usuarios interactúen con la app sin problemas y reciban respuestas adecuadas.

### Pruebas de la Lógica de Negocio
También se probaron aspectos clave de la lógica de la app, como cómo se manejan las respuestas y el conteo de puntos. Esto asegura que la app funcione bien y mantenga la integridad de los datos mientras los usuarios interactúan con ella.

### Ejecución de Pruebas en GitHub Actions
El pipeline de CI de **GitHub Actions** se configuró para ejecutar estas pruebas automáticamente cada vez que se realiza un `push` o `pull request` en la rama `main`. Esta automatización permite que los errores se detecten pronto y que la calidad del código se mantenga sin esfuerzo.

### Resultados de las Pruebas
Las pruebas se ejecutaron tanto en local como en el entorno de CI de GitHub Actions. Los resultados fueron positivos: los endpoints respondieron como se esperaba y la lógica de negocio funcionó bien, lo que confirmó que la app estaba lista para manejar distintos escenarios de uso sin problemas.

## Conclusión
Implementar pruebas y un sistema de CI con **GitHub Actions** mejoró la calidad de **QuizWiz** y dio más confianza en el código. Las pruebas automatizadas ayudan a que el desarrollo sea más rápido y seguro, reduciendo el riesgo de errores al añadir nuevas funciones o hacer cambios.
