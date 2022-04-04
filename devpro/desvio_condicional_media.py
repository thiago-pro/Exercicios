primeira_nota = float (input('Digite a primeira nota:'))
segunda_nota = float (input('Digite a segunda nota:'))
media_das_notas = (primeira_nota + segunda_nota) / 2
if (media_das_notas >= 7) & (media_das_notas < 10):
    print('Aluno aprovado!')
elif media_das_notas < 7:
    print('Aluno reprovado!')
elif media_das_notas >= 10:
    print('Aluno aprovado com distinção!')
