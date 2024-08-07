from flask import Flask, request, redirect, url_for
from flask_cors import CORS

import banco

app = Flask(__name__)
CORS(app)

@app.route("/get-produtos", methods=['GET'])
def ver_estoque():
    produtos = banco.verEstoque()
    for x in produtos:
        print(x)
    return produtos

@app.route("/alterar-estoque",  methods=['POST'])
def alterar_estoque():
    if request.method == 'POST':
        data = request.json
        print(data)
        banco.adicionarEstoque(data)
        return data
    #banco.adicionarEstoque()

@app.route("/atualizar-saldo", methods=['PATCH'])
def atualizar_saldo():
    if request.method == 'PATCH':
        data = request.json
        banco.atualizarSaldo(data)
        return data
