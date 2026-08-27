import os
os.system('cls')

#Entrada
print('=Solicitando Dados=')
primeiro_numero = int(input('Digite seu 1º número: '))
segundo_numero = int(input('Digite seu 2º número: '))

#Cálculos
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

#Mostrando o resultado
print('=Saida de Dados=')
print('Soma: ', soma)
print('subtracao: ', subtracao)
print('divisao: ', divisao)
print('multiplicacao: ', multiplicacao)
