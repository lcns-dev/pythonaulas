# Escreva um programa que leia dois numéros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior. / O segundo valor é maior / Não existe valor maior, os dois são iguais.
print("Vamos ver qual o número é maior?")
n1 = int(input("Escreva o primeiro número inteiro: "))
n2 = int(input("Escreva o segundo número inteiro: "))
if n1 > n2:
    print("O primeiro número é maior!")
elif n1 < n2:
    print("O segundo número é maior!")
else:
    print("Não existe valor maior, os dois são iguais.")