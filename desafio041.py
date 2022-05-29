# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta mostre sua categoria, de acordo com a idade:
# até 9 anos: mirim / até 14 anos: infantil / até 19 anos junior / até 20 anos sênior /acima: master.

from datetime import date
print('-=-' * 12)
print("CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print('-=-' * 12)
ano = int(input("Qual o ano de nascimento? "))
if date.today().year - ano <9:
    print("O inscrito nascido em {} com {} anos será da categoria Mirim.".format(ano, date.today().year - ano))
elif date.today().year - ano == 9 or date.today().year - ano < 14:
    print("O inscrito nascido em {} com {} anos será da categoria Infantil.".format(ano, date.today().year - ano))
elif date.today().year - ano == 14 or date.today().year - ano < 19:
    print("O inscrito nascido em {} com {} anos será da categoria Junior.".format(ano, date.today().year -ano))
elif date.today().year - ano == 19 or date.today().year - ano == 25:
    print("O inscrito nascido em {} com {} anos será da categoria Sênior.".format(ano, date.today().year - ano))
else:
    print("O inscrito nascido em {} com {} anos será da categoria Master.".format(ano, date.today().year - ano))