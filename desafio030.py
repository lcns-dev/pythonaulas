# Crie um programa que leia um número inteiro e mostre ne tela se ele é PAR ou ÍMPAR.
# Para esse exerciocio busquei a informação que ao usar o módulo que é representado por percentual "%" ele pode trazer,
# Valores de 1 e 0 podendo ser par ou ímpar.


num = int(input("Escolha um número: "))
par = num % 2
if par ==0:
    print("O número {} é par.".format(num))
else:
    print("O número {} é ímpar.".format(num))
