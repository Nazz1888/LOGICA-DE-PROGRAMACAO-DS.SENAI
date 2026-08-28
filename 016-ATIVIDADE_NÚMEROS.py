import os
os.system('cls')

#solicitação

numeroA = int(input('digite o 1º número: '))
numeroB = int(input('digite o 2º número: '))


#Processamento

media = (numeroA + numeroB) / 2

soma = numeroA + numeroB

produto = numeroA * numeroB

if numeroA > numeroB:
    print('O 1º número é Maior!')
else:
    print('O 2º número é Menor!')


valores = min(numeroA, numeroB)
valoresB = max(numeroA, numeroB)

#Resultado
print(f'soma é: {soma:.2f}')
print(f'produto é: {produto:.2f}')
print(f'media é: {media:.2f}')

if numeroA == numeroB:
    print('Os Números são Iguais!')
else:
    print(f'O menor é: {valores}')
    print(f'O maior é: {valoresB}')


