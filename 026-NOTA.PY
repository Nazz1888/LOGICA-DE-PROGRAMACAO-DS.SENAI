import os
os.system('cls')
#SOLICITAÇÃO
nota = int(input('Digite sua nota: '))
#PROCESSAMENTO
if nota == 0 or nota == 10:
    print(f'\n{nota}')
else:
    print(f'\nA nota deve ser entre 0 à 10')
