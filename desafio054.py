#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas dessas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#21 ano a maioridade

from datetime import date

hoje = date.today().year
contmaior = 0
contmenor = 0
for c in range(1, 8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = hoje - ano
    if idade <= 21:
        contmenor += 1
    else:
        contmaior += 1
print("Temos {} pessoas menores de idade.".format(contmenor))
print("Temos {} pessoas maiores de idade.".format(contmaior))
