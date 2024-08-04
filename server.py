from flask import Flask
from flask_cors import CORS

import banco

app = Flask(__name__)
CORS(app)

@app.route("/get-produtos")
def ver_estoque():
    produtos = banco.getEstoqueCompleto()
    return produtos

@app.route("/alterar-estoque")
def alterar_estoque():
    banco.adicionarEstoque()