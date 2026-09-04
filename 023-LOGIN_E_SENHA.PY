import os
os.system('cls')

#RECEBIMENTO
login = (input('Digite seu usuário: '))
senha = (input('Digite sua senha: '))

#PROCESSAMENTO
usuario_salvo = 'Yale'
senha_salva = '25'

usuario_correto = login == usuario_salvo
senha_correta = senha == senha_salva

#SAÍDA
if usuario_correto and senha_correta:
    print('Bem-vindo!')
else:
    print('Login ou senha inválidos.')