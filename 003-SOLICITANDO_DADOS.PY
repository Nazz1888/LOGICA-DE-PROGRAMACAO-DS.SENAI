import os
os.system("cls")#Linha usada para apagar a localização do arquivo do terminal.

#SOLICITANDO DADOS
#input adiciona o que for digitado no terminal na variável como texto.
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#int() converte o que for digitado em inteiro (números inteiros).
idade = int(input('Digite sua idade: '))

# float() converte o que foi digitado em float (números reais).
peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

#MOSTRANDO DADOS
print('Nome: ',  nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Peso: ', peso)
print('Altura: ', altura)
