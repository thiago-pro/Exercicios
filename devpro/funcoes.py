def triangulo (n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end= '   ')
        print('')

print('Triangulo com 1')
triangulo(1)

print('Triangulo com 2')
triangulo(2)

print('Triangulo com 3')
triangulo(3)
