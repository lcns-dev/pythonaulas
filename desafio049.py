#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, se que agora utilizando o laço for.

n = int(input("Escolha um número para aplicar na tabuada: "))
print("A tabuada do {} ficará assim:".format(n))
for c in range(1, 11):
    print("{} X {} = {}".format(c, n, c * n))
