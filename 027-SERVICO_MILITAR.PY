import os
os.system('cls')

#SOLICITAÇÃO
#O .strip() é para retirar os espaços em branco nas respostas. 
#E o .lower() serve para o código conseguir executar mesmo se as respostas forem maiúsculas ou minúsculas.
#Tanto o .strip() , quanto o .lower() só funcionam em variáveis de texto, em int ou float elas não irão funcionar.
sexo = str(input('Digite seu sexo de registro(masculino/feminino): ')).strip().lower()
nascimento = int(input('Digite seu ano de nascimento: '))

#PROCESSAMENTO
if nascimento <= 2008 and sexo == 'masculino':
    resultado = ('Apresentar-se para serviço militar obrigatório!')
else:
    resultado = ('Não deve se apresentar.')

#SAÍDA
print(f'\nResultado: {resultado}')
