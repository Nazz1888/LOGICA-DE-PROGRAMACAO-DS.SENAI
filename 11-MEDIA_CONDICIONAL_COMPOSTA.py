import os
os.system ('cls')

#Entrada
Primeira_nota = float (input('Digite a 1º nota: '))
segunda_nota = float (input('Digite a 2º nota: '))

#Processamento
soma = Primeira_nota + segunda_nota
media = soma / 2

if media >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')

#Resultado
print(f'Soma das notas', {soma})
print(f'Cálculo da media', {media})

