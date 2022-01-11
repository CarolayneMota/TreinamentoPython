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
"""