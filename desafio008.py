# Escreva um programa que leia um valor em metro e o exiba convertido em centímetros e milímetros.
n1 = float(input('Qual é a medida em metros? '))
print('Sua medida escolhida foi {}m, em centímetros teremos {:.0f} e em milímetros {:.0f}'.format(n1, n1*100, n1*1000))
