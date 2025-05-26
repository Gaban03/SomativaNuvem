from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)


db_config = {
    'host': 'db',
    'user': 'root',
    'password': '1234',
    'database': 'aero_solutions'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.json
    cpf = data['cpf']
    plano_saude = data['id_plano_saude']
    nome = data['nome']

    try:

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO paciente (cpf, id_plano_saude, nome) VALUES (%s, %s, %s)", (cpf, plano_saude, nome))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message" : "Cadastro realizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    

@app.route('/listar', methods=['GET'])
def listar():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT p.cpf, p.nome, ps.nome FROM paciente p LEFT JOIN plano_saude ps ON p.id_plano_saude = ps.id_plano_saude")
        dados = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(dados)
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

