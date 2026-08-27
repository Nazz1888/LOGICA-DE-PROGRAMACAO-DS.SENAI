import os
os.system('cls')

#Solicitação de Dados

salario_informado = float(input('Digite seu salário: '))

#Calculos

salario_minimo = 1621
quantidades_salarios = salario_informado / salario_minimo


#Mostrando resultados

print('=EXIBINDO DADOS=')
print(f'Quantidade de salários: ', {quantidades_salarios})