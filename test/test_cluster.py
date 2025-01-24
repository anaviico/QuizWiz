import requests
import psycopg2
import time

def test_api_endpoint():
    """Prueba si el endpoint principal responde correctamente."""
    url = "http://localhost:8000/"
    try:
        response = requests.get(url)
        assert response.status_code == 200
        print("✔ API endpoint funciona correctamente.")
    except Exception as e:
        print(f"✘ Error en el endpoint: {e}")

def test_database_connection():
    """Prueba si la base de datos es accesible y contiene datos."""
    try:
        conn = psycopg2.connect(
            dbname="quizwiz",
            user="postgres",
            password="root",
            host="localhost",
            port="5433"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions;")
        rows = cur.fetchall()
        assert len(rows) > 0
        print("✔ Conexión a la base de datos establecida y datos encontrados.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"✘ Error en la base de datos: {e}")

if __name__ == "__main__":
    print("Esperando a que el clúster esté activo...")
    time.sleep(10)  # Espera para que los contenedores estén listos
    test_api_endpoint()
    test_database_connection()
