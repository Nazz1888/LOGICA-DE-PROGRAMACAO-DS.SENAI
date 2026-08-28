import os
os.system('cls')

#Solicitações

idades = int(input('Digite a sua idade: '))

#Processamento
if idades < 16:
    print('Não podem votar!')
elif idades < 18:
    print('O voto é opcional!')
elif idades <= 65:
    print('O voto é obrigatório!')
else:
    print('Não é obrigado votar!')



