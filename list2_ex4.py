"""
Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do 
novo salário, reajustado de acordo com a tabela abaixo:
"""
salario_atual = float(input('Informe seu salário atual: '))
if salario_atual < 500:
    salario_novo = salario_atual + (salario_atual * 0.15)
    print(f'Salario com ajuste: R${salario_novo}')
elif salario_atual>= 500 and salario_atual <= 1000:
    salario_novo = salario_atual + (salario_atual * 0.10)
    print(f'Salario com ajuste: R${salario_novo}')
else:
    salario_novo = salario_atual + (salario_atual * 0.05)
    print(f'Salario com ajuste: R${salario_novo}')
