from flask import Flask, jsonify, request
from hamburgaria import Hamburgueria

app = Flask(__name__)

hamburgueria = Hamburgueria()


@app.route('/ver_cardapio', methods=["GET"])
def ver_cardapio():
    return jsonify(hamburgueria.get_cardapio())


@app.route('/adicionar_hamburguer', methods=["POST"])
def adicionar_cardapio():
    nome = request.json["nome"]
    ingredientes = request.json["ingredientes"]
    value = request.json["value"]
    hamburgueria.add_hamburguer(nome, ingredientes, value)
    return jsonify(message="Você adicionou o Hamburguer com sucesso")


@app.route('/ver_caixa', methods=["GET"])
def ver_caixa():
    return jsonify(hamburgueria.ver_caixa())


@app.route('/vender_hamburguer', methods=["POST"])
def vender_hamburguer():
    nome = request.args["nome"]
    hamburgueria.vender_de_hamburguer(nome)

    return jsonify(message=f"Você comprou um {nome}")
