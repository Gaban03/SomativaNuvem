from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# define as configurações para conexao com o banco de dados
db_config = {
    'host': 'db',
    'user': 'root',
    'password': '1234',
    'database': 'aero_solutions'
}

# rota padrao da pagina index do certificacao
@app.route('/')
def index():
    return render_template('index.html')

# rota para inserir no banco de dados
@app.route('/cadastrar_certificacoes', methods=['POST'])
def cadastrar():
    data = request.json
    id_mecanico = data['id_mecanico']
    apto = int(data['apto'])

    if id_mecanico is None or apto is None:
        return jsonify({"message": "Faltam dados obrigatórios"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO certificacao (id_mecanico, apto) VALUES (%s, %s)", (id_mecanico, apto))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message" : "Cadastro de certificação realizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    
# rota para consumir o banco de dados com select e retornar json para exibir no front
@app.route('/listar_certificacoes', methods=['GET'])
def listar():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id_certificacao, id_mecanico, apto FROM certificacao")
        certificacoes = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(certificacoes)
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

