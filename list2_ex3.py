"""
Faça um programa em que o usuário informe o salário recebido e o total gasto com despesas. Deverá ser 
exibido na tela “Gastos dentro do orçamento” caso o valor gasto não
ultrapasse o valor do salário e “Orçamento estourado” se o valor gasto
ultrapassar o valor do salário.
"""
salario = float(input('Informe o sálario recebido: '))
total = float(input('Informe o total gasto com despesas: '))
orcamento = salario - total
if orcamento > 0:
    print('Gastos dentro do orçamento')
else:
    print('Orçamento estourado')
