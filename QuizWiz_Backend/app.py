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

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.Config')

db.init_app(app)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
