from flask import Flask
from extensions import db
from config import Config, TestingConfig
from routes import bp
import os
import logging

# logger
logging.basicConfig(
    filename='quizwiz.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

logger.info("Iniciando aplicación QuizWiz!!")

app = Flask(__name__)

# entorno
if os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(Config)

app.secret_key = 'clavesecreta'

db.init_app(app)

app.register_blueprint(bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
