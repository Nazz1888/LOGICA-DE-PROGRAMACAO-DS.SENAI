import os
os.system('cls')

primeira_nota = float(input('Digite a 1º nota: '))
segunda_nota = float(input('Digite a 2º nota: '))
terceira_nota = float(input('Digite a 3º nota: '))

medias = (primeira_nota + segunda_nota + terceira_nota) / 3

if medias <= 7:
    print('Está reprovado')
else:
    print('Está aprovado')


print(f'Media: , {medias:.2f}')