"""
1 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = input("Informe seu nome: ")
    senha = input('Informe sua senha: ')
    if (nome != senha):
        print("Seu cadastro foi realizado!")
        break
    else:
         print("ERRO! Senha não pode ser seu nome, por favor mude sua senha. ")


Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input("Digite um valor entre 0 e 10: "))
    if (nota >= 0 and nota <= 10):
        print("Parabéns, o valor está entre 0 e 10: ")
        break
    else:
         print("Continue tentando, valor não está entre 0 e 10: ")

2 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
i = 1
while i >= 1 and i <=50:
    if i % 2 == 0:
        pass
    else:
        print(i)
    i += 1
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a 
soma dos valores.

lista = [9, 4, 3, 5, 10, 66, 100, 1]
print(f'Lista: {lista}')
lista.sort()
print(f'Lista ordenada: {lista}')
print(f'{lista[0]} + {lista[-1]} = {lista[0] + lista[-1]}')

------ Calculadora -----------
def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return num1/num2


def mult(num1, num2):
    return num1*num2


# Entrada
print("Escolha quan opeção deseja realizar: ")
opcao = input("+, -, /, *:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "+":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")
elif opcao == "-":
    valor_sub = sub(num1, num2)
    print(f'{num1} - {num2} == {valor_sub}')
elif opcao == "/":
    valor_div = div(num1, num2)
    print(f'{num1} / {num2} == {valor_div}')
elif opcao == "*":
    valor_mult = mult(num1, num2)
    print(f'{num1} * {num2} == {valor_mult}')
else:
    print('Opção invalida')

2 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses 
três argumentos.

def soma_tres(num1, num2, num3):
    return num1 + num2 + num3

print(f'soma_tres(1, 2, 3): ', soma_tres(1, 2, 3))

3 - Faça uma função que receba uma lista, percorra a lista e some a quantidade de números pares dessa lista 
e retorne a  soma. Imprimir a lista e o resultado da soma ao final do código.

def qtd_par_lista(lista):
    qtd_par = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            qtd_par += 1
        else:
            pass
    return qtd_par

lista = [1,2,3,2,1,2,3,4,5,6,5,4,3,2,1,8,10,12]
pares = qtd_par_lista(lista)
print(f'Lista: {lista}\nQuantidade de números pares: {pares}')

"""

