# Escreva um programa que leia um valor em metro e o exiba convertido em Km, Hectometros, Decametros, Decímetros, centímetros e milímetros.
n1 = float(input('Qual é a medida em metros? '))
print('Sua medida escolhida foi {}m, sendo assim teremos as seguintes medidas convertidas:'.format(n1))
print('Em Quilometros teremos {}'.format(n1/1000))
print('Em Hectometro teremos {}'.format(n1/100))
print('Em Decametros teremos {}'.format(n1/10))
print('Em Centímetros teremos{:.0f}'.format(n1*100))
print('Em Milímetros teremos {:.0f}'.format(n1*1000))
