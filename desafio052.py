# Faça um programa que leia um número inteiro e digite se ele é ou não um número primo.
import time #print("{}".format(c), end=" ")

print("Olá, vamos descobrir se o seu número é primo? ")
num = int(input("Digite um número: "))
cont = 0
for c in range(2, num):
        if num % c == 0:
            print("Multiplo de", c)
            cont += 1
if cont == 0:
    print("O número {} é primo".format(num))
else:
    print("O número {} não é Primo".format(num))