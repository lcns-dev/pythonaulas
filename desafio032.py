# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 1961
import calendar
ano = int(input("Qual ano quer analisar? "))
bis = calendar.isleap(ano)
if bis == True:
    print("O ano de {} é bissexto.".format(ano))
else:
    print("O ano de {} não é bissexto.".format(ano))