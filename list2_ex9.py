"""
  Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) 
  e informe se o resultado foi um empate, se a vitória foi do primeiro time ou do segundo time.
"""
gols_tA = int(input(f'Informe a quantidade de gols feitos pelo time A: '))
gols_tB = int(input(f'Informe a quantidade de gols feitos pelo time B: '))
if gols_tA == gols_tB:
    print('O resultado foi empate')
elif gols_tA > gols_tB:
    print('O time A venceu')
else:
    print('O time B ganhou')
