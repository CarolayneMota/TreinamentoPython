"""
Faça um programa em Python para encontrar a mediana de três valores inseridos pelo usuário.
"""
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))
if num1 > num2:
    if num1 < num3:
        mediana = num1
    elif num2 > num3:
        mediana = num2
    else:
        mediana = num3
else:
    if num1 > num3:
        mediana = num1
    elif num2 < num3:
        mediana = num2
    else:
        mediana = num3
print(f'Mediana: {mediana}')
