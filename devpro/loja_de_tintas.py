# Loja de tintas
# verificar a quantidade de tinta necessária para pintar a área mensionada

import math

valor_1 = 80
valor_2 = 25
area = int(input('digite o valor da area:'))
divisao = area / 6
resto = (divisao % 18)
lata = (divisao / 18)
if resto != 0:
    lata = int(lata + 1)

multiplicacao_01 = valor_1 * lata
print(f'Serão necessarios {int(lata)} latas de 18 litros totalizando R${multiplicacao_01:.2f}')
resto_02 = (divisao % 3.6)
galao = (divisao / 3.6)
if resto_02 != 0:
    galao = int(galao + 1)

multiplicacao_02 = valor_2 * galao
print(f'Serão necessarios {galao} galões de 3,6 litros totalizando R${multiplicacao_02:.2f}')
if math.floor(resto) <= 17:
    divisao_02 = (math.ceil(resto)) / 3.6
    multiplicacao_03 = (math.ceil(divisao_02)) * valor_2
    divisao_03 = divisao / 18
    multiplicacao_04 = (math.floor(divisao_03)) * valor_1
    soma = multiplicacao_03 + multiplicacao_04

if ((math.floor(divisao_03)) < 1) and galao == 1:
    print(f'Será necessario {galao} galão de 3,6 litros ao custo de {multiplicacao_02:.2f}')
elif ((math.floor(divisao_03)) < 1) and galao > 1:
    print(f'Serão necessarios {galao} galões de 3,6 litros ao custo de {multiplicacao_02:.2f}')
elif ((math.floor(divisao_02)) < 1) and lata == 1:
    print(f'Será necessario {int(lata)} lata de 18 litros ao custo de {multiplicacao_01:.2f}')
elif ((math.floor(divisao_02)) < 1) and lata > 1:
    print(f'Serão necessarias {int(lata)} latas de 18 litros ao custo de {multiplicacao_01:.2f}')
elif ((math.floor(divisao_03)) > 1) and ((math.floor(divisao_02)) >= 1):
    print(
        f'Serão necessarias {math.floor(divisao_03)} latas de 18 litros e {math.ceil(divisao_02)} galões de 3,6 litros ao custo de R${soma:.2f}')
