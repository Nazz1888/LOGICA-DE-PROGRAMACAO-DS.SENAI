import os
os.system('cls')

#SOLICITAÇÃO DE DADOS

Qmacas = int(input('Digite a quantidade de maçãs: '))

#PROCESSAMENT0 D0S DADOS
valorA = Qmacas * 1
valorD = Qmacas * 1.30

if Qmacas >= 12:
    print(f'\nValor a ser cobrado: R${valorA:.2f}')
else:
    print(f'\nValor a ser cobrado: R${valorD:.2f}')




