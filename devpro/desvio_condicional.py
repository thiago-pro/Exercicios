import math

pais_a = 80_000 # _ substitui o ponto no caso 80000
pais_b = 200_000
anos = 0

while pais_a <= pais_b:
    pais_a = pais_a * 1.03
    pais_b = pais_b * 1.015
    anos += 1
    if pais_a > pais_b:
        print(f'População do pais "A": {(math.floor(pais_a))}')
        print(f'População do pais "B": {(math.floor(pais_b))}')
        print(f'O pais "A" ultrapassa a população do pais "B" em {anos} anos!')
        break