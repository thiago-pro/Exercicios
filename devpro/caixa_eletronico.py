# Caixa eletrônico
# Sacar valores

saque = 0
while (saque < 10) or (saque > 600):
    saque = int(input('Digite o valor de saque - minimo R$10,00 máximo R$600,00:'))
    if (saque < 10) or (saque > 600):
        print('Valor inválido')

notas_de_100 = notas_de_50 = notas_de_10 = notas_de_5 = notas_de_1 = 0

notas_de_100, saque = divmod(saque, 100)
notas_de_50, saque = divmod(saque, 50)
notas_de_10, saque = divmod(saque, 10)
notas_de_5, saque = divmod(saque, 5)
notas_de_1, saque = divmod(saque, 1)

if notas_de_100 > 0:
    print(f'nota(s) de R$100,00: {notas_de_100}')

if notas_de_50 > 0:
    print(f'nota(s) de R$50,00: {notas_de_50}')

if notas_de_10 > 0:
    print(f'nota(s) de R$10,00: {notas_de_10}')

if notas_de_5 > 0:
    print(f'nota(s) de R$5,00: {notas_de_5}')

if notas_de_1 > 0:
    print(f'nota(s) de R$1,00: {notas_de_1}')