import equacao2 as eq
import math


a = float(input('Digite o valor de a = '))
b = float(input('Digite o valor de b = '))
c = float(input('Digite o valor de c = '))
if a !=0:
    delta = math.pow(b,2) - 4 * a * c
    if delta < 0:
        print(f'{a}x^2 + {b}x + {c} = 0\n')
        print(eq.menor_zero()) 
    elif delta == 0:
        print(eq.igual_zero(a, b, c))
    else:
        print(eq.bhaskara(a, b, c))
else:
    print('Não é equação do segundo grau')
