# Calculo do percentualde aumento de salário
print()
print("Siga os passos a seguir para saber o valor do aumento de sálrio!")
print()
salario = float(input("Digite o valor do salario!:"))
aumento = float(input("Digite qual a porcentagem do aumento de salario!:"))
print()
valor_aumento = float(salario * (aumento / 100))
salario_reajustado = valor_aumento + salario

print(f"O valor do reajuste foi de R$ {valor_aumento:.2f}")
print(f"O valor do salário reajustado é de R$ {salario_reajustado:.2f}")
