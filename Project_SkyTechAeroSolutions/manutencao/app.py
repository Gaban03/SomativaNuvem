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
    cpf_paciente = data['cpf_paciente']
    medico = data['medico']
    tipo_de_consulta = data['tipo_de_consulta']
    preco = data['preco']
    data_consulta = data['data_consulta']


    try:

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO consulta (cpf_paciente, medico, tipo_de_consulta, preco, data_consulta) VALUES (%s, %s, %s, %s, %s)", (cpf_paciente, medico, tipo_de_consulta, preco, data_consulta))
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

        cursor.execute("SELECT * FROM consulta")
        dados = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(dados)
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

