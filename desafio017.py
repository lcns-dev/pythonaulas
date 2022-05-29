#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot, floor
a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
hip = hypot(a, b)
print("O valor da sua hipotenusa é: {:.2f}" .format(hip))
