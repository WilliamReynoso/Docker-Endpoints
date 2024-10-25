import psycopg2
from psycopg2 import sql
from flask import Flask


app = Flask(__name__)
# Configuración de la conexión a la base de datos

def get_db_connection():
    connection = psycopg2.connect(
        host="db",
        database="docker_postgres_db2",
        user="postgres",
        password="password"
    )
    return connection

@app.route('/')
def home():
    return "Hello world!"

@app.route('/pagina')
def pagina():
    return "Esta es la página en el endpoint /pagina."

@app.route('/usuarios')
def usuarios():
    # Función para obtener la lista de usuarios de la base de datos
    try:
        # Establece la conexión con la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()
        # Consulta para obtener los usuarios
        query = sql.SQL("SELECT * FROM users")
        # Ejecuta la consulta
        cursor.execute(query)
        # Obtén todos los resultados
        users = cursor.fetchall()     
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"error": str(e)}

    return users

@app.route('/usuarios/torre')
def usuariostorre():
    # Función para obtener la lista de usuarios de la base de datos
    try:
        # Establece la conexión con la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()
        # Consulta para obtener los usuarios
        query = sql.SQL("SELECT * FROM users WHERE device = 'desktop'")
        # Ejecuta la consulta
        cursor.execute(query)
        # Obtén todos los resultados
        users = cursor.fetchall()     
        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return {"error": str(e)}

    return users
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
