#Crie um programa que leia dois valores e mostra um menu na tela
# [1] Somar
# [2] Mutiplicar
# [3] maior
# [4] novos números
# [5] Sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

import math
while True:
    print()
    num1 = int(input("Digite o 1º número: "))
    operador = input("Digite o operador matemático [ + - / * ]: ")
    num2 = int(input("Digite o 2º número: "))


    if operador == "+":
        print(int(num1 + num2))
    elif operador == "-":
        print(int(num1 - num2))
    elif operador == "/":
        print(int(int(num1 / num2)))
    elif operador == "*":
        print(int(num1 * num2))
    sair = input("Deseja sair? [s]im ou [n]ão: ")
    if sair == "s":
        break
