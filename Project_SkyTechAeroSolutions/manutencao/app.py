from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

'''Configuração do banco de dados do docker'''
db_config = {
    'host': 'db',
    'user': 'root',
    'password': '1234',
    'database': 'aero_solutions'
}

'''Rota padrão para a página inicial'''
@app.route('/')
def index():
    return render_template('index.html')

'''Rota para cadastrar a manutenção'''
@app.route('/cadastrar-manutencao', methods=['POST'])
def cadastro_manutencao():
    '''Faz um request com os dados enviados pelo FRONT-END'''
    data = request.json
    id_aeronave = data['id_aeronave']
    id_certificacao = data['id_certificacao']
    OS = data['OS']
    responsavel = data['responsavel']
    tipo_de_manutencao = data['tipo_de_manutencao']
    data_manutencao = data['data_manutencao']

    '''Verificação se os dados foram inseridos corrretamente'''
    if not id_aeronave:
        return jsonify({"message": "ID de aeronave obrigatório"}), 400

    if not id_certificacao:
        return jsonify({"message": "ID de certificação obrigatória"}), 400

    if not OS:
        return jsonify({"message": "OS obrigatória"}), 400
    
    if not responsavel:
        return jsonify({"message": "Responsável obrigatório"}), 400

    if not tipo_de_manutencao:
        return jsonify({"message": "Tipo de manutenção obrigatória"}), 400

    if not data_manutencao:
        return jsonify({"message": "Data da manutenção obrigatória"}), 400

    '''Faz um try catch para tratativa de possiveis erros'''
    try:
        '''Abre conexão com o banco de dados'''
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        '''Executa o script de inserção dos dados passados, para a tabela peca do banco de dados'''
        cursor.execute("INSERT INTO manutencao (id_aeronave, id_certificacao, OS, responsavel, tipo_de_manutencao, data_manutencao) VALUES (%s, %s, %s, %s, %s, %s)", (id_aeronave, id_certificacao, OS, responsavel, tipo_de_manutencao, data_manutencao))
        conn.commit()

        '''Fecha a conexão com o banco de dados'''
        cursor.close()
        conn.close()

        '''Retorna uma mensagem dizendo que o cadastro deu certo e o status 201'''
        return jsonify({"message" : "Cadastro realizado com sucesso!"}), 201
    except Exception as e:
        '''Retorna o erro caso algo tenha dado errado e o status 500'''
        return jsonify({"message" : str(e)}), 500
    

'''Rota para listar todos os registros de manutenção'''
@app.route('/listar-manutencao', methods=['GET'])
def listar():
    try:
        '''Abre conexão com o banco de dados'''
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        '''Executa um script SQL de consulta no banco que retorna todos os dados da tabela peca'''
        cursor.execute("SELECT id_manutencao, id_aeronave, id_certificacao, OS, responsavel, tipo_de_manutencao, data_manutencao FROM manutencao")
        dados = cursor.fetchall()

        '''Fecha a conexão com o banco de dados''' 
        cursor.close()
        conn.close()

        '''Retorna uma mensagem dizendo que a consulta deu certo e o status 200'''
        return jsonify(dados), 200
    except Exception as e:
        '''Retorna o erro caso algo tenha dado errado e o status 500'''
        return jsonify({"message" : str(e)}), 500

'''Função de inicialização do arquivo app.py'''   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

