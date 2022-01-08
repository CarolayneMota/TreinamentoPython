"""
1 -
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
else:
    print(f'{num2} é maior que {num1}')

2-
num = float(input('Informe um número: '))
if num > 0:
    print(f'{num} é positivo')
else:
    print(f'{num} é negativo')

3-
peso = float(input('Informe o peso em Kg: '))
h = float(input('Informe a altura em m: '))
imc = peso/(h**2)
if imc < 18.5:
    print(f'Seu IMC é {imc} e você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc} e você está no peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc} e você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc} e você está com obesidade')
else:
    print(f'Seu IMC é {imc} e você está com obesidade mórbida')

4-
letra = input('Informe a letra F ou M: ')
if letra == 'F':
    print('F - Feminino')
elif letra == 'M':
    print('M - Masculino')
else:
    print('Sexo Inválido')

5-
letra = input('Informe uma letra e saiba de é vogal ou consoante: ')
if letra == 'a' or letra == 'A':
    print(f'A letra {letra} é vogal')
elif letra == 'e' or letra == 'E':
    print(f'A letra {letra} é vogal')
elif letra == 'i' or letra == 'I':
    print(f'A letra {letra} é vogal')
elif letra == 'o' or letra == 'O':
    print(f'A letra {letra} é vogal')
elif letra == 'u' or letra == 'U':
    print(f'A letra {letra} é vogal')
else:
    print(f'A letra {letra} é consoante')

6-
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    
    if media == 10:
        print('Aprovado com Distinção')
    else:
        print('Aprovado')
else:
    print('Reprovado')

7-
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')

8-
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))
if num1 > num2 and num1 > num3:
    print(f'O maior número é {num1}')
    if num2 < num3:
        print(f'O menor número é {num2}')
    else:
        print(f'O menor número é {num3}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é {num2}')
    if num1 < num3:
        print(f'O menor número é {num1}')
    else:
        print(f'O menor número é {num3}')
else:
    print(f'O maior número é {num3}')
    if num2 < num1:
        print(f'O menor número é {num2}')
    else:
        print(f'O menor número é {num1}')

9-
num1 = float(input('Informe o preço em reais do primeiro produto: '))
num2 = float(input('Informe o preço em reais do segundo produto: '))
num3 = float(input('Informe o preço em reais do terceiro produto: '))
if num1 < num2 and num1 < num3:
    print(f'O protudo 1 deve ser comprado por ter o preço R${num1}')
elif num2 < num1 and num2 < num3:
    print(f'O protudo 2 deve ser comprado por ter o preço R${num2}')
else:
    print(f'O protudo 3 deve ser comprado por ter o preço R${num3}')

10-
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
num3 = float(input('Informe o terceiro número: '))
if num1 > num2 and num1 > num3:
    if num2 < num3:
        print(f'Ordem: {num1}, {num3},{num2}')
    else:
        print(f'Ordem: {num1}, {num2},{num3}')
elif num2 > num1 and num2 > num3:
    if num1 < num3:
        print(f'Ordem: {num2}, {num3},{num1}')
    else:
        print(f'Ordem: {num2}, {num1},{num3}')
else:
    if num2 < num1:
        print(f'Ordem: {num3}, {num1},{num2}')
    else:
        print(f'Ordem: {num3}, {num2},{num1}')

11-
turno = input(f'Em que turno você estuda?\nM-matutino ou V-Vespertino ou N- Noturno\nR: ')
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')

12-
num = int(input('Informe um número: '))
if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')

13-
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1+n2)/2
if media <= 10 and media > 9:
    print(f'Média: {media}\nConceito: A')
elif media <= 9 and media > 7.5:
    print(f'Média: {media}\nConceito: B')
elif media <= 7.5 and media > 6:
    print(f'Média: {media}\nConceito: C')
elif media <= 6 and media > 4:
    print(f'Média: {media}\nConceito: D')
elif media <= 4 and media > 0:
    print(f'Média: {media}\nConceito: E')
else:
    print('Não possui conceito')

14-
dia = int(input('Informe um número de 1 à 7: '))
if dia == 1:
    print('1 - Domingo')
elif dia == 2:
    print('2 - Segunda')
elif dia == 3:
    print('3 - Terça')
elif dia == 4:
    print('4 - Quarta')
elif dia == 5:
    print('5 - Quinta')
elif dia == 6:
    print('6 - Sexta')
elif dia == 7:
    print('7 - Sábado')
else:
    print('Valor inválido')

15-
print('Menu\n1. Água\n2. Refrigerante\n3. Suco')
escolha = int(input('Digite o número correspondente a bebida que você deseja: '))
if escolha == 1:
    print(f'Você escolheu água!')
elif escolha ==2:
    print(f'Você escolheu refrigerante!')
elif escolha == 3:
    print(f'Você escolheu suco!')
else:
    print('Não existe bebida correspondente ao número informado')

"""

