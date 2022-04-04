s1 = input('Digite uma string: ')
s2 = input('Digite uma string a ser comparada com a primeira: ')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'"{s1}": {tamanho1} caracteres')
print(f'"{s2}": {tamanho2} caracteres')

comparacao_de_tamanho = 'diferente'
comparacao_de_conteudo = 'diferente'

if s1 == s2:
    comparacao_de_tamanho = 'Iguais'
    comparacao_de_conteudo = 'igual'
elif tamanho1 == tamanho2:
    comparacao_de_tamanho = 'Iguais'

print(f'As duas strings são de tamanhos {comparacao_de_tamanho}.')
print(f'As duas strings são de conteudo {comparacao_de_conteudo}.')