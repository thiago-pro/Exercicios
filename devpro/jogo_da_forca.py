palavra = 'Thiago'.upper()

print('Jogo da forca')
print('Descubra a palavra!')

print('A palavra é: ',
      end='')  # metodo end= não pula linha de um print para outro que tbm tenha end=, semelhante a concatenação
for letra in palavra:
    print(f'_ ', end='')

conjunto_letras_palavras = set(
    palavra)  # set cria um conjunto com as letras fazendo com que seja possivel realizar comparação dos elementos  ex: a letra T consta no conjunto Thiago?
conjunto_letras_digitadas = set()  # criado um conjunto vazio
erros = 0
#conjunto_letras_palavras.issubset(conjunto_letras_digitadas)           #issubset representa o conten ex: o conjunto palavra contem a letra do conjunto letras digitada

while not conjunto_letras_palavras.issubset(conjunto_letras_digitadas) and erros < 7:              #enquanto nao conter a letra no conjunto palavra execute
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)       #add adiciona uma letra ao conjunto
    if letra_digitada in conjunto_letras_palavras:
        print('A palavra é: ', end='')
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print(f'_ ', end='')
    else:
        erros += 1
        print(f'->Erro {erros} de 6. Tente novamente!')
        print()
        print(f'Letras ja digitadas: ', conjunto_letras_digitadas)

if erros < 7:
    print('Parabens, você ganhou!!')
else:
    print('Você perdeu!')
