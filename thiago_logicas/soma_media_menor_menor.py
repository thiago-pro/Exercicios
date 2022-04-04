# verificador: maior numero, menor numero, quantidade de numeros
# impar e par soma dos numeros, media dos numeros digitados

contador_1 = 0
contador_2 = 0
soma = 0
contador_par = 0
contador_impar = 0

while True:
    numero = int(input("Digite um numero para somar ou zero para sair!:"))
    if numero == 0:
        break
    while contador_1 < 1:
        maior = numero
        menor = numero
        contador_1 += 1

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    if (numero % 2) == 0:
        contador_par += 1
    else:
        contador_impar += 1

    soma = int(numero) + int(soma)
    contador_2 += 1
    media = soma / contador_2

print()
print(f"O maior numero digitado foi o numero: {maior}")
print(f"O menor numero digitado foi o numero: {menor}")
print(f"A quantidade de numeros impar digitados foi de: {contador_impar}")
print(f"A quantidade de numeros par digitados foi de: {contador_par}")
print(f"A soma dos numeros digitados foi de: {soma}")
print(f"A média dos numeros digitados foi de: {media:.1f}")
