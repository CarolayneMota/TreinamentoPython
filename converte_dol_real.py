"""
Faça um programa que peça um valor em dólares e converta pra um valor em reais e
mostre na tela  o resultado da conversão.
FORMULA: 1 dólar = 5.68 reais
"""
print(f'\nConverte o valor em dólares para real\n')
v_dol = float(input('Informe o valor em dólares: '))
convet = v_dol*5.68
print(f'O valor em reais de ${v_dol} dólares é R${convet}\n')
