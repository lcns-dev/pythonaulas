# Desenvolva um programa que leia 6 númeroa inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconcidere-o.

print("Vamos somar somente os números pares, pode iniciar !")
s = 0
for num in range(1, 7):
    num = int(input("Digite o {}° valor: ".format(num)))
    if num % 2 == 0:
        s+= num
print("A soma entre eles é {}".format(s))
