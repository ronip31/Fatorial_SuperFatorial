from flask import Flask, jsonify

app = Flask(__name__)

def calcular_fatorial(numero):
    if not isinstance(numero, int):
        return "Número deve ser um número inteiro."
    elif numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = []
        fatorial = 1
        for i in range(1, numero+1):
            fatorial *= i
            resultado.append(fatorial)
        return resultado

def super_fatorial(numero):
    if not isinstance(numero, int):
        return "Número deve ser um número inteiro."
    elif numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        val = 1
        ans = []
        for i in range(1, numero + 1):
            val *= i
            ans.append(val)
        arr = [1]
        for i in range(1, len(ans)):
            arr.append(arr[-1] * ans[i])
        return arr

@app.route('/fatorial/<int:numero>')
def obter_fatorial(numero):
    resultado = calcular_fatorial(numero)
    return jsonify({'resultado': resultado})

@app.route('/superfatorial/<int:numero>')
def obter_superfatorial(numero):
    resultado = super_fatorial(numero)
    return jsonify({'resultado': resultado})

@app.route('/fatorial/<float:numero>')
@app.route('/superfatorial/<float:numero>')
def numero_invalido(numero):
    return "Número inválido. Por favor, forneça um número inteiro."

if __name__ == '__main__':
    app.run(debug=True)
