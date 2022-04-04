def validar(ip:str) -> bool:
    numeros = ip.split('.')  # o ponto é o objeto separador do split, neste caso.

    if len(numeros) != 4:
        return False

    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False
    return True

ips_validos = []
ips_invalidos = []
with open('ips.txt', 'r') as arquivo: #O arquivo ips foi criado e acrescentado alguns valores 'r' para ler dados do arquivo
    for linha in arquivo:
        ip = linha.strip() # remove o conta barra n elimina as linhasem
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open('ips_saida.txt', 'w') as arquivo: #'w para escrever ou acrescentar dados a um arquivo, no caso ips_saida'
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')
    arquivo.writelines('[Endereços inválidos:]\n')

    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')
