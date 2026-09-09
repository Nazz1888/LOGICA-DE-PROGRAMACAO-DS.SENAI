import os
os.system('cls')

#SOLICITAÇÃO
valorP = float(input('Digite o valor do produto: '))
forma_pagamento = (input('Digite a forma de pagamento(V/P): '))

#PROCESSAMENTO
Vista = valorP * 0.10
Parcelado = valorP / 6

match valorP:
    case 'V':
        print(Vista)
    case 'P':
        print(Parcelado)
    case _:
        print('INVÁLIDO')

#SAÍDA
