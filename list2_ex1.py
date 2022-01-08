"""
Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.
"""
num = int(input('Informe um número: '))
if num > 0:
    print(f'{num} é positivo')
elif num < 0:
    print(f'{num} é negativo')
else:
    print(f'{num} é neutro')

    