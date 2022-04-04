class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro:float, quantidade_combustivel:float):
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valor_litro
        self._apresentar_valor_se_possivel(litros_abastecidos, valor)

    def _apresentar_valor_se_possivel(self, litros_abastecidos:float, valor:float):
        if litros_abastecidos > self.quantidade_combustivel:
            print(f'Não é possivel realizar o abastecimento, faltam {litros_abastecidos - self.quantidade_combustivel} litros')
            print('Reabasteça a bomba!')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litroas, a um valor de R${valor:.2f}')
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros {self.tipo_combustivel}')

    def abastecer_por_litro(self, litros_abastecidos:float):
        valor = litros_abastecidos * self.valor_litro
        self._apresentar_valor_se_possivel(litros_abastecidos, valor)

    def adicionar_combustivel(self, quantidade:float):
        if quantidade >= 0:
            self.quantidade_combustivel += quantidade
        else:
            print('Voce nao vai roubar combustivel')


bomba = BombaCombustivel('Gasolina', 4.56, 100)
bomba.abastecer_por_valor(100)
bomba.abastecer_por_litro(50)

bomba.valor_litro = 6

bomba.adicionar_combustivel(-200)