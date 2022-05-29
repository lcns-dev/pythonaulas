# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguai, o aumento é de 15%.
import math
sal = float(input("Qual o salário do funcionário? "))
sup = float(sal*10)/100+sal
inf = float(sal*15)/100+sal
if sal <=1250:
    print("Quem ganhava R${:.2f} agora irá ganhar R${:.2f}.".format(sal, inf))
else:
    print("Quem ganhava R${:.2f} agora irá ganahr R${:.2f}.".format(sal, sup))
