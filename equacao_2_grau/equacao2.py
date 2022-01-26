import math

def bhaskara(formulario):
    a = float(formulario.txt_a.text())
    b = float(formulario.txt_b.text())
    c = float(formulario.txt_c.text())

    if a != 0:
        delta = math.pow(b, 2) - 4 * a * c
        if delta < 0:
            formulario.lbl_resultado.setText(
                f'{a}x^2 + {b}x + {c} = 0\nEsta equação não possui raízes reais')

        elif delta == 0:
            x1 = -b/2*a
            formulario.lbl_resultado.setText(
                f'{a}x^2 + {b}x + {c} = 0\nA raiz desta equação é {x1}')
        else:
            x2 = (-b + math.sqrt(delta)) / (2*a)
            x3 = (-b - math.sqrt(delta)) / (2*a)
            if x2 < x3:
                formulario.lbl_resultado.setText(
                    f"{a}x^2 + {b}x + {c} = 0\nX1 = {x2}\nX2= {x3}")
            else:
                formulario.lbl_resultado.setText(
                    f"{a}x^2 + {b}x + {c} = 0\nX1 = {x3}\nX2= {x2}")
    else:
        formulario.lbl_resultado.setText('Não é equação do segundo grau')
