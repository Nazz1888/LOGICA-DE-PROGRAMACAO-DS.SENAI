import os
os.system('cls')

#SOLICITAÇÃO
matricula = int(input('Digite o número da sua matrícula: '))
anos_trabalho = int(input('Digite a quantos anos trabalha na empresa: '))
ano_nascimento = int(input('Digite o ano em que nasceu: '))

#PROCESSAMENTO
if anos_trabalho >=30 or anos_trabalho <= 1961:
    Aposentadoria = ('Requerer aposentadoria.')
else:
    Aposentadoria = ('Não requerer aposentadoria.')

#SAÍDA
print(f'\nMatrícula:  {matricula}')
print(f'Anos de trabalho:  {anos_trabalho}')
print(f'Ano de nascimento:  {ano_nascimento}')
print(f'Aposentadoria:  {Aposentadoria}')
