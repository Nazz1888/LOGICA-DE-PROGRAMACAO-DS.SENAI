import os
os. system('cls')

#SOLICTAÇÃO
aluno = input('Digite seu nome: ')
nota1 = float(input('Digite sua 1º nota: '))
nota2 = float(input('Digite sua 2º nota: '))

#PROCESSAMENTO

media = (nota1 + nota2) / 2

#VISUALIZAÇÃO

print(f'Sua Media é: {media:.1f}')
if media >= 9:
  print('Aprovado! Nota A')
elif media >=7.5:
  print('Aprovado! Nota B')
elif media >=6:
  print('Aprovado! Nota C')
elif media >=4:
  print('Reprovado! Nota D')
else:
  print('Reprovado! Nota E')
