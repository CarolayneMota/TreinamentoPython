"""
Escrever um programa em Python para ler um número inteiro e informar se ele é divisível por 5.
"""
num = int(input('Informe um número: '))
if num % 5 == 0:
    print(f'{num} é divisível por 5')
else:
    print(f'{num} não é divisível por 5')
