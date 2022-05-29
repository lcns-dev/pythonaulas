# Faça um programa que leia o ano de um jovem e informe, conforme a sua idade:
# Se ele ainda vai se alistar ao serviço / Se é a hora de se alistar. / Se já passou do tempo do alistamento.
# O seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


import calendar
from datetime import date
count = 0
print("Alistamento do Governo Brasileiro.")
nome = input("Qual o seu nome? ")
ano = int(input("Qual o ano de nascmimento? "))
if date.today().year - ano < 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(ano, date.today().year - ano, date.today().year))
    print("Ainda faltam {} anos para o alistamento.".format(18 - (date.today().year - ano)))
    print("{} seu alistamento será em {}.".format(nome, ano + 18))
elif date.today().year - ano > 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(ano, date.today().year - ano, date.today().year))
    print("Você já deveria ter se alistado há {} anos.".format((date.today().year - ano) - 18))
    print("{} seu alistamento foi em {}.".format(nome, ano + 18))
elif date.today().year - ano == 18:
    print("Quem nasceu em {} tem {} anos em {}.".format(ano, date.today().year - ano, date.today().year))
    print("{} você deve se alistar IMEDIATAMENTE!".format(nome))
