#Crie um algorítimo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.
n = int(input('Escolha um número: '))
print('O dobro do valor de {} é {} \nO triplo de {} é {} \nE a raiz quadrada de {} do valor é {:.2f}'.format(n, n*2, n, n*3, n, n**(1/2)))
