from flask import Flask, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as rotas e origens

db_config = {
    'host': 'db',
    'user': 'root',
    'password': '1234',
    'database': 'aero_solutions'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anat_mock', methods=['GET'])
def listar():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute('''SELECT m.id_mecanico, m.nome, m.cpf, c.apto FROM mecanico m LEFT JOIN certificacao c ON m.id_mecanico = c.id_mecanico;''')
        dados = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(dados)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
