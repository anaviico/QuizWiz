from flask import Flask
from models import db
from routes import bp
from sqlalchemy.sql import text

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5433/quizwiz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'clavesecreta'

db.init_app(app)

# Registrar el blueprint
app.register_blueprint(bp)

# Ruta básica para verificar la conexión
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
