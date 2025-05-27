from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# configurações para conexao do banco de dados
db_config = {
    'host': 'db',
    'user': 'root',
    'password': '1234',
    'database': 'aero_solutions'
}

# rota padrao da pagina de mecanico
@app.route('/')
def index():
    return render_template('index.html')

# rota para cadastar um mecanico no banco de dados 
@app.route('/cadastrar_mecanico', methods=['POST'])
def mecanico():
    data = request.json
    nome = data['nome']
    cpf = data['cpf']

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute(""" INSERT INTO mecanico (nome, cpf) VALUES (%s, %s) """,(nome, cpf))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message" : "Cadastro de mecanico realizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# rota para consumir os dados do banco com um select e transformar em json para exibir no front
@app.route('/listar_mecanico', methods=['GET'])
def listar():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id_mecanico, nome, cpf FROM mecanico")
        dados_mecanico = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(dados_mecanico)
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
