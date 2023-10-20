from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/sumar_numeros', methods=['POST'])
def sumar_numeros():
    try:
        datos = request.get_json()
        numero1 = datos['numero1']
        numero2 = datos['numero2']
        numero3 = datos['numero3']

        # Realiza la suma y agrega 2 a cada número
        resultado = numero1 + numero2 + numero3 + 2

        # Devuelve el resultado como respuesta JSON
        return jsonify({"resultado": resultado})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
