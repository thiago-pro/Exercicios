# Tabuada

print()

valor = int(input("Digite um numero para saber a sua tabuáda!:"))
contador = 0

while contador < 11:
    print(f"{valor} X {contador} = {valor * contador}")
    contador += 1
