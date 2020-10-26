import os
from flask import Flask, jsonify, request

app = Flasck (_name_)

@app.route('/')
def nao_entre_em_panico():
    prox = 1
    ant = 0
    maximo = 50
    n = 0
    resposta = "0 -"
    while (n < maximo):
        fibo = prox
        prox = prox + ant
        ant = fibo
        n = n+1
        resposta+= str(prox) + "-"


    return resposta

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host= '0.0.0.0', port=port)
