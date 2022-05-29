#Desafio Faça um programa que leia a largura e a altura da uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
alt = float(input('Qual é a altura de sua parede? '))
comp = float(input('Qual o comprimento da parede? '))
m2 = alt * comp
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m'.format(alt, comp, m2))
print('Você irá precisa de {:.2f}L de tinta para pintar a parede toda.'.format((alt*comp)/2))
