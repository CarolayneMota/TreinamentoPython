"""
1 - Crie um programa que tenha uma lista de 5 frutas, e depois adicione uma nova fruta no final da lista.
Depois remova o primeiro elemento da lista e por fim, altere o valor do item 2 pra "banana"
lista = ['maçã', 'banana','uva', 'mamão', 'pera']
print(lista)
lista.append('melão')
print(lista)
lista.pop(0)
lista[1] = 'banana'
print(lista)
2 - Crie uma lista com os dados de 4 pessoas (nome, idade, sexo, ano_nascimento).
Dica:  Usar lista de lista
dados = []
print(dados)
dados.append(['Carolayne', 20, 'Feminino', 2001])
dados.append(['Maria Victoria', 20, 'Feminino', 2001])
dados.append(['Thammara', 20, 'Feminino', 2001])
dados.append(['Jennife', 20, 'Feminino', 2001])
print(dados)

lista_pessoas = [["Mario", "Carvalho", "Campo Grande", 1997, 85],
                 ["Pedro", "Campos", "Campo Grande", 1994, 78],
                 ["Elisa", "Vitória", "Campo Grande", 2000, 45]]

print(lista_pessoas[0])

# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima npo final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    # Adicionar  o endereço, adicionar  o peso
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite seu peso da pessoa: "))
    endereco = input('Digite o endereço da pessoa: ')
    nova_pessoa = [nome, idade, peso, endereco]
    lista_pessoas.append(nova_pessoa)

for pessoa in lista_pessoas:
    print(f" Bem-vin@ {pessoa[0]}! Você tem {pessoa[1]} anos e pesa {pessoa[2]}Kg. Você mora no endereço {pessoa[3]}.")
    if pessoa[1] > 18:
        print(f'{pessoa[0]}, você é maior de idade!')
    else:
        print(f'{pessoa[0]}, você é menor de idade')
print("Quantidade de pessoas cadastradas: ", len(lista_pessoas))
"""
