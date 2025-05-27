# Importando o que vamos usar: Flask (framework web), request (pra pegar os dados que chegam), 
# jsonify (pra mandar respostas em JSON), e render_template (pra carregar páginas HTML)
from flask import Flask, request, jsonify, render_template
#Importando o conector do MySQL pra se conectar com o banco de dados
import mysql.connector
# Criando a aplicação Flask
app = Flask(__name__)
# Configurações pra conectar no banco de dados
db_config = {
    'host': 'db',
    'user': 'root',
    'password': '1234',
    'database': 'aero_solutions'
}
# Rota principal para quando acessar o site
@app.route('/')
def index():
    return render_template('index.html')
# Rota pra cadastrar uma aeronave
@app.route('/cadastrar_aeronave', methods=['POST'])
def cadastrar_aeronave():
    # Pega os dados que vieram no corpo da requisição em JSON
    data = request.json
    modelo = data['modelo']
    fabricante = data ['fabricante']
    horas_voo = data['horas_voo']
      # Verificações básicas: se algum campo obrigatório estiver faltando, retorna erro
    if not modelo:
        return jsonify ({"message": "Modelo de Aeronave necessário para cadastro"}),400

    if not fabricante:
        return jsonify ({"message": "Necessario o fabricante para cadastro"}),400
    
    if not horas_voo:
        return jsonify ({"message": "Necessario as horas de voo "}),400

    try:
        # Tenta se conectar ao banco
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
         # Executa o INSERT no banco com os dados da aeronave
        cursor.execute("INSERT INTO aeronaves (modelo, fabricante, horas_voo) VALUES (%s, %s, %s)", (modelo, fabricante, horas_voo))
         # Salva as mudanças no banco
        conn.commit()
         # Fecha a conexão com o banco
        cursor.close()
        conn.close()
         # Retorna resposta de sucesso
        return jsonify({"message" : "Cadastro realizado com sucesso"}), 201
    except Exception as e:
        # Se algo der errado, mostra o erro
        return jsonify({"message" : str(e)}), 500
    
# Rota pra listar todas as aeronaves cadastradas
@app.route('/listar_aeronaves', methods=['GET'])
def listar_aeronaves():
    try:
        # Conecta no banco
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Busca todos os dados da tabela aeronaves
        cursor.execute("SELECT id_aeronave, modelo, fabricante, horas_voo FROM aeronaves")
        # Pega todos os resultados
        dados = cursor.fetchall()

        cursor.close()
        conn.close()
        # Retorna os dados encontrados em formato JSON
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    # Inicia a aplicação Flask rodando na porta 5000 e acessível de qualquer IP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

