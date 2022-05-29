# Faça um programa que calcule a soma de todos os números ímpares multiplos de 3 e se encontre entre 1 e 500.

s = 0
for num in range(1, 500, 2):
    if num % 3 == 0:
        s = s + num
print("A soma de 1 a 500 é: {}".format(s))