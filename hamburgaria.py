class Hamburgueria():

    def __init__(self):
        self.caixa = float()
        self.cardapio = []

    def add_hamburguer(self, nome_hamburguer, ingredientes, value):

        hamburguer = {
            "nome": nome_hamburguer,
            "ingredientes": ingredientes,
            "value": value
        }

        self.cardapio.append(hamburguer)

    def get_cardapio(self):
        return self.cardapio

    def vender_de_hamburguer(self, nome_hamburguer):

        for hamburguer in self.cardapio:
            if nome_hamburguer == hamburguer["nome"]:
                self.caixa += hamburguer["value"]

    def ver_caixa(self):
        return self.caixa


h = Hamburgueria()
