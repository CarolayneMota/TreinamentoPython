import math

def bhaskara(a, b, c):
    if a !=0:
        delta = math.pow(b,2) - 4 * a * c
        x2 = (-b + math.sqrt(delta))/ (2*a)
        x3 = (-b - math.sqrt(delta))/ (2*a)
        if x2 < x3:
             return f"{a}x^2 + {b}x + {c} = 0\nX1 = {x2}\nX2= {x3}"
        else:
            return f"{a}x^2 + {b}x + {c} = 0\nX1 = {x3}\nX2= {x2}"


def menor_zero():
    return f'Esta equação não possui raízes reais'   

def igual_zero(a, b, c):
    delta = math.pow(b,2) - 4 * a * c
    x1 = -b/2*a
    return f'{a}x^2 + {b}x + {c} = 0\nA raiz desta equação é {x1}'
