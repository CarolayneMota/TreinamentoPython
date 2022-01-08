"""
Faça um programa em Python para calcular a soma e a média de n números inteiros inseridos pelo usuário. Digite 0 para terminar.
"""
print("Insira os números. Digite 0 para sair: ")
contador = 0
soma = 0.0
num = 1

while num != 0:
   num = int(input(""))
   soma = soma + num
   contador += 1
if contador == 0:
   print("Digite alguns números")
else:
    print(f'Soma dos números: {soma}')
    print(f'Média: {soma/(contador-1)}')
