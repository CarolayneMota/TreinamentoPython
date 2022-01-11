"""
1 - 
Faça um Programa que leia 5 números inteiros, insira em uma lista e
mostre-os.

lista = []
for i in range(5):
    num = int(input('Informe um número: '))
    lista.append(num)
print(f'Lista: {lista}')

2-
Faça um Programa que leia 10 números reais, insira em uma lista e
mostre-os na ordem crescente (use a função sort())

lista = []
for i in range(10):
    num = float(input('Informe um número: '))
    lista.append(num)
lista.sort()
print(f'Lista: {lista}')

3-
Faça um Programa que leia N (peça pro usuário informar o valor de N) notas
e insira em uma lista, depois percorra a lista e calcule a soma das notas, por
fim calcule a média (soma dividido por N) e mostre na tela.

lista = []
soma = 0
n = int(input('Informe o valor N: '))
for i in range(n):
    num = float(input('Informe um número: '))
    lista.append(num)
for i in range(n):
    soma = soma + lista[i]
media = soma/n
print(f'A media é {media}')

4-
Faça um Programa que peça o nome, a idade e a altura de N pessoas,
armazene cada informação em uma lista e depois insira em uma lista maior chamada lista_pessoas. 
Por fim, imprima o nome e peso de cada pessoa, e diga se ela é maior ou menor de idade.

lista_pessoas = []
qtd_pessoas = int(input('Informe a quantidade de pessoass que vai cadastra: '))
for  i in range(qtd_pessoas):
    lista_pessoas.append([])
    nome = input('Informe o nome: ')
    lista_pessoas[i].append(nome)
    idade = int(input('Informe a idade: '))
    lista_pessoas[i].append(idade)
    altura = float(input('Informe a altura: '))
    lista_pessoas[i].append(altura)
print(f'Dados: {lista_pessoas}')

for i in range(qtd_pessoas):
    if lista_pessoas[i][1] > 18:
        print(f'{lista_pessoas[i][0]} é maior de idade!')
    else:
        print(f'{lista_pessoas[i][0]} é menor de idade!')


5-

6-

7-

8-

9-

10 -

----------Desafios----------
1-

2-

"""
