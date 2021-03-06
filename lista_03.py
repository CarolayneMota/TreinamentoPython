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
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do
outro.(usar for com range)

for i in range(1, 21):
    print(i)

6-
Faça um programa que leia 5 números e informe o maior número.(Dica: Use
lista, função .sort() e indexação negativa (pegar i item [-1]))
v = []
for i in range(5):
    num = float(input('Informe um número: '))
    v.append(num)
v.sort()
print(f'Entre os números informados {v[-1]} é o maior')

7-
Faça um programa que imprima na tela apenas os números ímpares entre 1
e 50.(Use range de intervalos (range(x, y)))
for i in range(1, 51):
    if i % 2 == 0:
        pass
    else:
        print(i)

8-
Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles.(Use range de
intervalos (range(x, y)))
x = int(input('Informe um número para iniciar o intervalo: '))
y = int(input('Informe um número para finalizar o intervalo: '))
for i in range(x+1, y):
    print(i)

9-
Faça um programa que, dado um conjunto de N números, determine o menor
valor, o maior valor e a soma dos valores.
v = [2, 5, 7, 10, 4]
v.sort()
print(f'Menor valor: {v[0]}\nMaior valor: {v[-1]}\nSoma: {v[0]} + {v[-1]} = {v[0] + v[-1]}')

10 -
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual número ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
print('\tGerador de tabuada')
num = int(input('Informe um número inteiro entre 1 a 10: '))
if num >= 1 and num <= 10:
    print(f'Tabuada de {num}:')
    for i in range(1,11):
        print(f'{num} x {i} = {num * i}')
else:
    print('Número invalido')

----------Desafios----------
1-
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça
um programa capaz de gerar a série até o N ésimo termo., onde N é inserido pelo
usuário.
print('Sequência de Fibonacci')
n = int(input('Informe o limete superior: '))
d1 = 0
d2 = 1
d3 = d1 + d2
print(f'{d2} -> {d3}', end='')
while n > d3:
    d1 = d2
    d2 = d3
    d3 = d1 + d2
    print(f' -> {d3}', end='')
print('\n')

2-
Faça um programa que crie uma matriz NxN, insira os valores e imprima em
formato de matriz.
# para construir a matriz
dim = int(input('Informe as dimensões da matriz: '))
matriz = []
for i in range(dim):
    matriz.append([])
    for j in range(dim):
        num = int(input('Número: '))
        matriz[i].append(num)
print('\nMatriz')
# para imprimir a matriz
linhas = len(matriz)
colunas = len(matriz[0])
for i in range(linhas):
    for j in range(colunas):
        if j == colunas - 1:
            print(f'{matriz[i][j]}', end="")
        else:
            print(f'{matriz[i][j]}', end=' ')
    print()

"""
