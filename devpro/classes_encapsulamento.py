class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
            self.idade += 1

otavio = Pessoa('otavio', 2, 12, 80)

for _ in range(22):
    otavio.envelhecer()
    print(f'Idade {otavio.nome} é: {otavio.idade} anos. E sua altura é {otavio.altura} cm')