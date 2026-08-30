import os
os. system('cls')

#SOLICTAÇÃO
aluno = input('Digite seu nome: ')
nota1 = float(input('Digite sua 1º nota: '))
nota2 = float(input('Digite sua 2º nota: '))

#PROCESSAMENTO E VISUALIZAÇÃO

media = (nota1 + nota2) / 2

print(f'Sua Media é: {media:.1f}')
if media >= 9:
  print('Aprovado!')
elif media >=6:
  print('Aprovado!')
else:
  print('Reprovado!')
  
  