import os
os.system('cls')

primeiro_numero = int(input('Digite o 1º número: '))
segundo_numero = int(input('Digite o 2º número: '))
terceiro_numero = int(input('Digite o 3º número: '))

maior = max(primeiro_numero,  segundo_numero, terceiro_numero)

menor = min(primeiro_numero,  segundo_numero, terceiro_numero)


print(f'\nO 1º é: {primeiro_numero}')
print(f'O 2º é: {segundo_numero}')
print(f'O 3º é: {terceiro_numero}')
print(f'o maior é: {maior}')
print(f'O menor é: {menor}')
