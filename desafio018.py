#Faça um programa que leia um ângulo qualquer e mostre ne tela o valor do seno, cosseno e tengente desse ângulo.
import math

import trigonometry
num = float(input('Qual o valor do ângulo? '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O valor do seno é: {:.2f}'.format(sen))
print('O valor do cosseno é: {:.2f}'.format(cos))
print('O valor da tangente é: {:.2f}'.format(tan))
