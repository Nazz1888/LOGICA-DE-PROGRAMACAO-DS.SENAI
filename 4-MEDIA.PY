import os
os.system("cls")  # Limpa a tela do terminal

print('= Solicitando Dados =')
nome =  input('digite seu nome: ')
idade = int(input('digite sua idade '))
primeira_nota = float (input('digite a primeira nota: '))
segunda_nota = float (input('digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

print('\n= Exibindo Dados =')
print('Nome:  ', nome)
print('Idade:  ', idade)
print('Primeira nota:  ', primeira_nota)
print('Segunda nota:  ', segunda_nota)
print('Média:  ', media)

#\n é usado para pular uma linha no terminal.
# ATALHOS DO VSCODE: alt + shift + seta para baixo é usado para duplicar a linha de código e move-lá. ctrl + F5 para abrir o terminal e Ctrl + J para fechar o terminal.
if media >= 7:
    print('aluno aprovado')
else:
    print('aluno reprovado')
    