"""
1 - Crie um programa que peça o ano de nascimento e calcule a idade e verifique SE a pessoa é maior de idade.
MAIOR DE IDADE: idade >= 18
MENOR DE IDADE: < 18
Saída: 
Imprimir a idade
Imprimir a mensagem dizendo se é maior ou menor de idade

"""
ano = int(input('Informe o ano do seu nascimento: '))
ano_atual = 2021
idade = ano_atual - ano

if idade >= 18:
  print(f"Idade: {idade}\nMaior de idade")  
else:
  print(f"Idade: {idade}\nMenor de idade")
