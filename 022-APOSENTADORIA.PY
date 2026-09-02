import os
os.system('cls')

matricula = int(input('Digite o código da matrícula: '))
nascimento = int(input('Digite o ano do seu nascimento: '))
Ttrabalho = int(input('Digite a quanto tempo você trabalha: '))


print(f'Código do emppregado: {matricula}')
print(f'Ano de nascimento: {nascimento}')
print(f'Tempo na empresa: {Ttrabalho}')



if Ttrabalho >= 30:
    print('Apto a aposentadoria, passí vel de requerimento.')
elif nascimento <=1960:
    print('apto aposentadoria, passível de requerimento.')
else:
    print('Inapto a aposentadoria, requerimento negado!')