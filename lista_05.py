"""
1 -
def pos_neg(valor):
    if valor > 0:
        return True
    else:
        return False

print(pos_neg(-5))
print(pos_neg(5))

2 -
def par_imp(valor):
    if valor % 2 ==0:
        return True
    else:
        return False
print(par_imp(1))
print(par_imp(2))

3 -
def soma(n1, n2, n3):
    return n1+n2+n3

print(soma(1,2,3))

4 -
def pos_neg(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'

print(pos_neg(-5))
print(pos_neg(5))

5 -
def qtd_dig(num):
    qtd = str(num)
    return len(qtd)

print(qtd_dig(5))
print(qtd_dig(15))

6 -
def novo_salario(s_atual, por):
    porcentagem = por/100
    novo = s_atual + s_atual*porcentagem 
    return novo

print(novo_salario(100,10))

7 -
import math
def vol_esfera(raio):
    volume = (4/3)*math.pi*(raio**3)
    return volume
print(vol_esfera(10))

8 -
def media(n1,n2,n3,tipo):
    if tipo.upper() == 'A':
        m_ari =(n1+n2+n3)/3
        return m_ari
    elif tipo.upper() == 'P':
        m_pon = ((n1*5)+(n2*3)+(n3*2))/(5+3+2)
        return m_pon
    elif tipo.upper() == 'H':
        m_har = 3/((1/n1)+(1/n2)+(1/n3))
        return m_har
    else:
        return 'Tipo de média não existente'

print(media(1,2,3,'A'))
print(media(1,2,3,'p'))
print(media(1,2,3,'h'))

9 -
def primo(valor):
    resul = 0
    i = 2
    while i <= valor // 2:
        if valor % i == 0:
            resul = resul + 1
        i = i + 1

    if resul == 0:
        return True
    else:
        return False

print(primo(2))
print(primo(6))

10 -
def dias(anos, meses, dias):
    dias_ano = anos * 365
    dias_meses = 30
    dias_total = dias_ano + dias_meses + dias
    return f'Quatidade de dias que você viveu: {dias_total}'

print(dias(20,4,19))

11-
def categoria(idade):
    if idade>= 5 and idade<=7:
        return 'Infantil A'
    elif idade>= 8 and idade<=10:
        return 'Infantil B'
    elif idade>= 11 and idade<=13:
        return 'Juvenil A'
    elif idade>= 14 and idade<=17:
        return 'Juvenil B'
    else:
        return 'Adulto'

print(categoria(6))
print(categoria(9))
print(categoria(12))
print(categoria(15))
print(categoria(20))
12 -
def conceito(media):
    if media>= 0.0 and media<= 4.9:
        return 'D'
    elif media>= 5.0 and media<= 6.9:
        return 'C'
    elif media>= 7.0 and media<= 8.9:
        return 'B'
    else:
        return 'A'

print(conceito(3))
print(conceito(6))
print(conceito(8))
print(conceito(9))

13 -
def peso_ideal(alt, sexo):
    if sexo.upper() == 'M':
        ideal = 72.7 * alt - 58
        return ideal
    elif sexo.upper() == 'F':
        ideal = 62.1 * alt - 44.7
        return ideal
    else:
        return 'ERRO'

print(peso_ideal(1.7,'F'))
print(peso_ideal(1.7,'M'))

pip install matplotlib
Desafios
1 -

2 -

"""



