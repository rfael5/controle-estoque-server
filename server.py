from flask import Flask, request, redirect, url_for
from flask_cors import CORS

import banco

app = Flask(__name__)
CORS(app)

@app.route("/get-produtos", methods=['GET'])
def ver_estoque():
    produtos = banco.verEstoque()
    return produtos


@app.route("/alterar-estoque",  methods=['POST'])
def alterar_estoque():
    if request.method == 'POST':
        data = request.json
        banco.adicionarEstoque(data)
        return data
    

@app.route("/atualizar-saldo", methods=['PATCH'])
def atualizar_saldo():
    if request.method == 'PATCH':
        data = request.json
        banco.atualizarSaldo(data)
        return data


@app.route("/historico", methods=["GET"])
def get_historico():
    historico = banco.getEstoqueCompleto()
    return historico


@app.route("/historico-periodo", methods=["GET"])
def get_historico_periodo():
    args = request.args
    data_inicio = args.get('data_inicio')
    data_fim = args.get('data_fim')
    historico = banco.buscarHistoricoPeriodo(data_inicio, data_fim)
    return historico

