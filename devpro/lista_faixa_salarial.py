salarios = [200, 250, 320, 400, 480, 600, 700, 710, 999, 1000, 2000, 3000]
contagen_de_faixa_salarial = [0] * 9
for salario in salarios:
    indice = salario // 100 - 2
    indice_maximo = len(contagen_de_faixa_salarial) - 1
    indice = min(indice, indice_maximo)
    contagen_de_faixa_salarial[indice] += 1

print(contagen_de_faixa_salarial)