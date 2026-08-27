import os
os.system('cls')

primeiro_numero = float(input('digite o 1º número: '))
segundo_numero = float(input('digite o 2º número: '))

media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero / segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

#min-Para descobrir o menor número, max-para se descobrir o maior.
#Outra possibilidade:
# if primeiro_numero > segundo_numero:
#   maior = primeiro_numero
#    menor = segundo_numero
#else:
#    maior = segundo_numero
#    menor = primeiro_numero


print(f'Media:  , {media:.2f}')
print(f'Soma:  , {soma:.2f}')
print(f'Produto:  , {produto:.2f}')
print(f'Maior é:  , {maior}')
print(f'Menor é:  , {menor}')
