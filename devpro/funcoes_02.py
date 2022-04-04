def quadrado (n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end= '   ')

        print('')


print('Triangulo com 1')
quadrado(1)

print('Triangulo com 2')
quadrado(2)

print('Triangulo com 3')
quadrado(3)