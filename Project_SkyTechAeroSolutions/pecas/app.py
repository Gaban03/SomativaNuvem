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

'''Rota para cadastrar a peça'''
@app.route('/cadastrar-peca', methods=['POST'])
def cadastro_peca():
    '''Faz um request com os dados enviados pelo FRONT-END'''
    data = request.json
    id_manutencao = data.get('id_manutencao')
    peca = data.get('peca')
    quantidade = data.get('quantidade')

    '''Verificação se os dados foram inseridos corrretamente'''
    if not id_manutencao:
        return jsonify({"message": "ID Manutenção obrigatório"}), 400

    if not peca:
        return jsonify({"message": "Peça obrigatória"}), 400

    if not quantidade:
        return jsonify({"message": "Quantidade obrigatória"}), 400

    '''Faz um try catch para tratativa de possiveis erros'''
    try:
        '''Abre conexão com o banco de dados'''
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        '''Executa o script de inserção dos dados passados, para a tabela peca do banco de dados'''
        cursor.execute("INSERT INTO pecas (id_manutencao, peca, quantidade) VALUES (%s, %s, %s)", (id_manutencao, peca, quantidade))
        conn.commit()

        '''Fecha a conexão com o banco de dados'''
        cursor.close()
        conn.close()

        '''Retorna uma mensagem dizendo que o cadastro deu certo e o status 201'''
        return jsonify({"message": "Cadastro realizado com sucesso!"}), 201
    except Exception as e:
        '''Retorna o erro caso algo tenha dado errado e o status 500'''
        return jsonify({"message": str(e)}), 500

'''Rota para listar todos os registros de peças'''
@app.route('/listar-pecas', methods=['GET'])
def listar_pecas():
    try:
        '''Abre conexão com o banco de dados'''
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        '''Executa um script SQL de consulta no banco que retorna todos os dados da tabela peca'''
        cursor.execute("SELECT id_pecas, id_manutencao, peca, quantidade FROM pecas")
        dados = cursor.fetchall()

        '''Fecha a conexão com o banco de dados'''
        cursor.close()
        conn.close()

        '''Retorna uma mensagem dizendo que a consulta deu certo e o status 200'''
        return jsonify(dados), 200
    except Exception as e:
        '''Retorna o erro caso algo tenha dado errado e o status 500'''
        return jsonify({"message": str(e)}), 500

'''Função de inicialização do arquivo app.py'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
