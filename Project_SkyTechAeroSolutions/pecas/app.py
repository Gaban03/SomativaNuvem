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

@app.route('/consultas-paciente', methods=['POST'])
def consultas_paciente():
    data = request.json
    cpf = data.get('cpf')

    if not cpf:
        return jsonify({"message": "CPF obrigatório"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT id_consulta, medico, tipo_de_consulta, preco, data_consulta
            FROM consulta
            WHERE cpf_paciente = %s
            ORDER BY data_consulta DESC
        """, (cpf,))

        consultas = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({"consultas": consultas})
    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
