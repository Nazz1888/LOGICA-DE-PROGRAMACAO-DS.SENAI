import os
os.system('cls')

#from datetime import date
#date.today().year, usado para trabalhar com datas, anos nesse caso.
#print(f'Data: {date.today()}')

#SOLICITAÇÃO
matricula = int(input('Digite o número da sua matrícula: '))
anos_trabalho = int(input('Digite a quantos anos trabalha na empresa: '))
ano_nascimento = int(input('Digite o ano em que nasceu: '))

#PROCESSAMENTO
if anos_trabalho >=30 or ano_nascimento <= 1961:
    Aposentadoria = ('Requerer aposentadoria.')
else:
    Aposentadoria = ('Não requerer aposentadoria.')

#SAÍDA
print('\n==RESULTADO==')
print(f'Matrícula:  {matricula}')
print(f'Anos de trabalho:  {anos_trabalho}')
print(f'Ano de nascimento:  {ano_nascimento}')
print(f'Aposentadoria:  {Aposentadoria}')
