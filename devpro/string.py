nome = input('Digite seu nome: ').upper()

nome_invertido_por_letras = ''.join(reversed(nome))
nome_invertido_por_palavras = ' '.join(reversed(nome.split()))# O espaço entre '' determina o espaço entre as palavras em nome_inertido_palavras
#metodo split separa as palavras digitadas
print(f'Nome com letras em maiusculo {nome}')
print(f'Nome com letras em maiusculo invertido por letras {nome_invertido_por_letras}')
print(f'Nome com letras em maiusculo invertido por palavras {nome_invertido_por_palavras}')

