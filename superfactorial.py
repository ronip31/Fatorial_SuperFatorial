from flask import Flask, jsonify
import redis
from decimal import Decimal, getcontext

app = Flask(__name__)
cache = redis.Redis()

def calcular_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return Decimal(1)
    else:
        cache_key = f"fatorial:{numero}"
        resultado = cache.get(cache_key)
        if resultado:
            return Decimal(resultado.decode())

        fatorial = Decimal(1)
        for i in range(1, numero + 1):
            fatorial *= Decimal(i)

        cache.set(cache_key, str(fatorial))
        return fatorial

def calcular_super_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return Decimal(1)
    else:
        cache_key = f"super_fatorial:{numero}"
        resultado = cache.get(cache_key)
        if resultado:
            return Decimal(resultado.decode())

        super_fatorial = Decimal(1)
        for i in range(1, numero + 1):
            super_fatorial *= calcular_fatorial(i)

        cache.set(cache_key, str(super_fatorial))
        return super_fatorial

@app.route('/super_fatorial/<int:numero>', methods=['GET'])
def obter_super_fatorial(numero):
    getcontext().prec = 50  # Define a precisão decimal para 50 dígitos

    resultado = calcular_super_fatorial(numero)
    return jsonify({'numero': numero, 'super_fatorial': str(resultado)})

if __name__ == '__main__':
    app.run(debug=True)
