"""
1 -
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
soma = num1 + num2
print(f'{num1} + {num2} = {soma}')

2 -
n_1 = float(input('Informe o primeiro nota: '))
n_2 = float(input('Informe a segunda nota: '))
n_3 = float(input('Informe a terceira nota: '))
n_4 = float(input('Informe a quarta nota: '))
media = (n_1+n_2+n_3+n_4)/4
print(f'\nPrimeiro nota: {n_1}\nSegunda nota: {n_2}\nTerceira nota: {n_3}\nQuarta nota:{n_4}\nMédia: {media}')

3 -
print(f'Convete de metros(m) em centrimetros(cm)\n')
cm = float(input('Informe o comprimento em centrimetros(cm): '))
m = cm/100
print(f'{cm}cm = {m}m')

4 -
print(f'Calcule a aréa do círculo\n')
raio = float(input('Informe o raio em cm: ')) 
area =  3.14 * (raio**2)
print(f'A área do círculo de raio {raio} é {area}cm')

5 -
print(f'Área do quadrado\n')
tam = float(input('Informe o tamanho do lado em cm: '))
area = tam**2
dobro = area*2
print(f'A área do quadrado de lado {tam}cm é {area}cm e o dobro dessa área é {dobro}cm')

6 -
print(f'Cálculo do salário mensal ')
din = float(input('Quanto você ganha por hora: '))
hora = float(input('Quantas horas você trabalha por mês: '))
salario = din *hora
print(f'Salário do mês R${salario}')

7 -
print(f'De graus Fahrenheit para graus Celsius\n')
F = float(input(f'Informe a temperatura em graus Fahrenheit: '))
C = 5 * ((F-32) / 9)
print(f'{F}F = {C}C')

8 -
num1_int = int(input('Informe o primeiro número inteiro: '))
num2_int = int(input('Informe o segundo número inteiro: '))
num3_real = float(input('Informe o primeiro número real: '))

e_1 = (num1_int*2) * (num2_int/2)
e_2 = (num1_int*3) + num3_real
e_3 = num3_real**3

print(f'o produto do dobro do primeiro com metade do segundo: {e_1}\nsoma do triplo do primeiro com o terceiro: {e_2}\no terceiro elevado ao cubo: {e_3}')

9 -
print(f'Saiba qual seria seu peso ideal de acordo com sua altura\n')
altura = float(input('Informe sua altura em m: '))
peso = (72.7*altura) - 58
print(f'O peso ideal para altura de {altura}m é de {peso}Kg')

10 -
print(f'Saiba qual seria seu peso ideal de acordo com sua altura\n')
h = float(input('Informe sua altura em m: '))
homem = (72.7*h) - 58
mulher = (62.1*h) - 44.7
print(f'O peso ideal para altura de {h}m para homem é {homem}Kg e para mulher é {mulher}')

"""



