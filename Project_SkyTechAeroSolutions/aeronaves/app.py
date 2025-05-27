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

@app.route('/cadastrar_aeronave', methods=['POST'])
def cadastrar_aeronave():
    data = request.json
    modelo = data['modelo']
    fabricante = data ['fabricante']
    horas_voo = data['horas_voo']
    
    if not modelo:
        return jsonify ({"message": "Modelo de Aeronave necessário para cadastro"}),400

    if not fabricante:
        return jsonify ({"message": "Necessario o fabricante para cadastro"}),400
    
    if not horas_voo:
        return jsonify ({"message": "Necessario as horas de voo "}),400

    try:

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO aeronaves (modelo, fabricante, horas_voo) VALUES (%s, %s, %s)", (modelo, fabricante, horas_voo))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message" : "Cadastro realizado com sucesso"}), 201
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    

@app.route('/listar_aeronaves', methods=['GET'])
def listar_aeronaves():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id_aeronave, modelo, fabricante, horas_voo FROM aeronaves")
        dados = cursor.fetchall()

        cursor.close()
        conn.close()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"message" : str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

