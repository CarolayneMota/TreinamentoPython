"""
1 - Crie um programa que receba o dia, mês e ano de nascimento de uma pessoa. Use a biblioteca datatime 
pra verificar o dia da semana que a pessoa nasceu. 

import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_br")

ano = int(input('Informe o ano do seu nascimento: '))
mes = int(input('Informe o mês do seu nascimento: '))
dia = int(input('Informe o dia do seu nascimento: '))
data_nasc = datetime.datetime(ano,mes,dia)
print(f'Você nasceu na data {dia}/{mes}/{ano} e nessa data era {data_nasc.strftime("%A")}')

"""
