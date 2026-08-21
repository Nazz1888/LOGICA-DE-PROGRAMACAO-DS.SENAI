#Limpa o terminal

import os
os.system("cls")

print('Solicitando Dados =')
valor = float(input('Digite o valor: '))

#CALCULANDO
#DESCONTO DE 10%

desconto =  valor * 0.10
valor_com_desconto = valor - desconto
print('\n= EXIBINDO DADOS = ')
print('Valor com desconto de 10%: ', valor_com_desconto)

print('Se quiser mais é só roubando')
