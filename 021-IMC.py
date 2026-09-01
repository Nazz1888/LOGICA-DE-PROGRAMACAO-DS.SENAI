import os
os.system('cls')

#PROCESSAMENTO
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

#CALCULO E VISUALIZAÇÃO
imc = peso /  (altura * 2)

print(f'O seu IMC é: {imc:.1f}')

if imc <18.5:
    print('Abaixo do peso!')
elif imc <=24.9:
    print('Peso ideal!')
elif imc <=29.9:
    print('Levemente acima do peso!')
elif imc <=34.9:
    print('Obesidade grau I!!')
elif imc <=39.9:
    print('Obesidade grau II!!!')
else:
    print('Obesidade III!!!')