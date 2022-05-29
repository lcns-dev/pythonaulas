# Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.


lista = []
qnt = input("Quantos pesos vamos avaliar? ")
for c in range(1, int(qnt)+1):
    lista.append(float(input("Digite o peso do {}º: ".format(c))))
print("O maior peso é {:.2f}Kg.".format(max(lista)))
print("O menor peso é {:.2f}Kg.".format(min(lista)))
