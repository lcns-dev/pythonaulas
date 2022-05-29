# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
la = float(input("Qual a medida do 1º lado? "))
lb = float(input("Qual a medida do 2º lado? "))
lc = float(input("Qual a medida do 3º lado? "))
if la+lb > lc and lb+lc > la and lc+la > lb:
    print("Poderá formar o triângulo.")
else:
    print("Não poderá formar o triângulo")