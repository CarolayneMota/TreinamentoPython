"""
1 -
lista = []
print('Programa que add os números informados em uma lista. Caso queira encerrar o programa digite zero(0).')
while True:
    num = float(input('Informe um número: '))
    if num == 0:
        break
    else:
        lista.append(num)
print(f'Lista: {lista}')

2 - 
nome = input("Informe seu nome: ")
senha = input('Informe sua senha: ')
while True:
    if (nome != senha):
        print("Senha aceita")
        break
    else:
        print("Senha Inválida")
        senha = input('Informe sua senha: ')

3 -
n = int(input('Informe um número inteiro: '))
i = 1
soma = 0
while i <= n:
    soma += i
    i+=1
print(soma)

4 -
n = int(input('Informe um número inteiro: '))
i = 2
soma = 0
while i <= n:
    if i % 2 == 0:
        soma += i
    i+=1
print(soma)

5 -
num = int(input('Informe um número inteiro: '))
while True:
    if num % 2 == 0:
        print(f'{num} é par')
        break
    else:
        num = int(input('Informe um número inteiro: '))

6 -
imp = 0
par = 0
i = 1
while i<=10:
    num = int(input('Informe um número inteiro: '))
    if num % 2 == 0:
        par +=1
    else:
        imp +=1
    i+=1
print(f'Quantidade de número par: {par}\nQuantidade de número ímpar: {imp}')
  
"""
      