# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
nome = input('Qual o nome do funcionário? ')
s = float(input('Qual o salário do {}? R$'.format(nome)))
print('O valor atual do salário de {} é R${:.2f} e com um aumento de 15% ele irá receber R${:.2f}'.format(nome, s, (s+(s*15)/100)))
