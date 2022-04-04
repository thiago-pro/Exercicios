notas = []

while True:
    entrada = input('Digite um numero!')
    if entrada == '-1':
        break
    notas.append(float(entrada))

tamanho = len(notas)  # extrair o tamanho de uma lista
print(f'Foram lidas {tamanho} notas')
print(' '.join([str(nota) for nota in notas]))  # converção da lista para string
notas.reverse()  # inverte a posição dos elementos de uma lista

for nota in notas:
    print(nota)

soma = sum(notas)  # somatoria de todos os elemnetos de uma lista
media = soma / tamanho
print(f'A soma das notas é: {soma}')
print(f'A média das notas é: {media}')

print('Notas acima da média')
print(' '.join([str(nota) for nota in notas if
                nota > media]))  # é possivel colocar condições, no caso notas apenas acima da media serão sisualizadas

print('Notas abaixo da média')
print(' '.join([str(nota) for nota in notas if nota < 7]))

print('Programa de estatistica encerrado!')
