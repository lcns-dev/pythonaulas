#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu entecessor.
n1 = int(input('Escolha um numero: '))
print('O sucessor de {}, é {}'.format(n1, n1+1), end=' ')
print('e seu antecessor será {}.'.format(n1-1))
