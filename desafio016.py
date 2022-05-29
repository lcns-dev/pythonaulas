#Crie um programa que leia um número real qualquer pelo teclado e mostre ne tela a sua porção inteira.
from math import floor

num = float(input('Digite um número: '))
print('O número {}, tem a parte inteira {}.'.format(num, floor(num)))
