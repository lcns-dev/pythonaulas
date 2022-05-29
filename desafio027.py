#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeira e o último nome separadamente.
# Ex. Ana Maria de Souza / Primeiro: Ana / Último: Souza
nome = str(input("Qual o seu nome completo? ")).strip()
print("Prazer em te conhecer!")
print("Primeiro nome é {}".format(nome.split()[0]))
print("Último nome é {}".format(nome.split()[-1]))
