"""
Escreva um programa em Python para calcular o fatorial de qualquer número inteiro.
"""
print('Fatorial de um número')
factorial = 1
num = int(input('Informe um número para calcular: '))
if num < 0:
    print('Não existe fatorial para número negativo')
elif num == 0:
    print('O fatorial de 0 é 1')
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'O fatorial de {num} é {factorial}')
