import os
os.system('cls')
#RECEBIMENTO
media = float(input('Digite sua media: '))
faltas = int(input('Digite suas faltas: '))

#PROCESSAMENTO
limite_de_faltas = 40
media_de_aprovacao = 7
if media >= media_de_aprovacao and faltas <= limite_de_faltas:
    resultado = ('Aluno Aprovado!')
else:
    resultado = ('Aluno Reprovado.')
# SAÍDA

print(f'\nResultado: {resultado}')