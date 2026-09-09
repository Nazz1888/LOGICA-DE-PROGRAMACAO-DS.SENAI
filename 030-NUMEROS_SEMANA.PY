import os
os.system('cls')

#SOLICITAÇÃO

dia = int(input('Digite um número para o dia da semana: '))


#PROCESSAMENTO
match dia:
    case 1 | 6 :
        print('Final de semana')
    case 2 | 3 | 4 | 5 :
        print('Dia útil')
    case _:
        print('Dia inválido')
#SAÍDA
print('=== FIM ===')