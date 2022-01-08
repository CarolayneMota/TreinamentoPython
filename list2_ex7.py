"""
Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3 valores a, b e c. Se 
o valor de i é par então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário, se 
i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. Os pesos dos 
valores são respectivamente 2, 3 e 4.
"""
i = int(input('Informe o valor i: '))
if i > 0:
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: '))
    if a > 0 and b > 0 and c > 0:

        if i % 2 == 0:
            media_ari = (a+b+c)/3
            print(f'Média aritmética: {media_ari}')
        elif i > 10:
            media_ari = (a+b+c)/3
            media_pon = (a*2 + b*3 + c*4)/9
            print(f'Média aritmética: {media_ari}\nMédia ponderada: {media_pon}')
else:
    print('i precisa ser positivo')
