from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as rotas e origens

db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'password',
    'database': 'medical_clinic_db'
}

@app.route('/planos', methods=['GET'])
def listar_planos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id_plano_saude, nome FROM plano_saude")
        dados = cursor.fetchall()

        cursor.close()
        conn.close()

        planos = [{"id": row[0], "nome": row[1]} for row in dados]

        return jsonify(planos)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
