print("calculo Fibonacci!")
print()

valor_final = input("Digite o valor final para o fibonacci!:")
valor_anterior = 1
valor_atual = 0
resultado = 0

while int(resultado) <= int(valor_final):
    print(valor_atual)
    resultado = valor_anterior + valor_atual
    valor_anterior = valor_atual
    valor_atual = resultado