#Crie um programa que leia o nome completo da pessoa e mostre:
#1. O nome com todas as letras maiúculas.
#2. O nome com todas as letras minúsculas.
#3. Quantas letras ao total (sem conciderar os espaços).
#4. Quantas letras tem o primeiro nome.
#Leandro Camacho Nunes da Silva
print("Vamos usar as variáveis para o seu nome.")
nome = str(input("Qual o seu nome completo? "))
completo = nome.strip().split()
print("O seu nome com todas as letras minúsculas: {}".format(nome.lower()))
print("O seu nome com todas as letras maiúsculas: {}".format(nome.upper()))
print('O seu nome tem {} letras ao total.'.format(len(nome) - nome.count(' ')))
print("O seu primeiro nome tem {} letras.".format(len(completo[0])))
