from flask import Flask
from models import db
from routes import bp
from sqlalchemy.sql import text
from config import Config, TestingConfig
import os

app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(Config)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5433/quizwiz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'clavesecreta'

db.init_app(app)

app.register_blueprint(bp)

@app.route('/')
def index():
    try:
        db.session.execute(text('SELECT 1'))
        return 'Conectado a la base de datos exitosamente'
    except Exception as e:
        return f'Error al conectar a la base de datos: {e}'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
