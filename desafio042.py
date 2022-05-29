# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais. / Isósceles: dois lados iguais. / Escaleno: todos os lados diferentes.

la = float(input("Qual a medida do 1º segmento? "))
lb = float(input("Qual a medida do 2º segmento? "))
lc = float(input("Qual a medida do 3º segmento? "))
if la+lb > lc and lb+lc > la and lc+la > lb:
    print("Poderá formar o triângulo.")
    if la == lb and lb == lc:
        print("Seu triângulo é EQUILÁTERO, isso acontece pois todos os lados são iguais!")
    if la == lb == lc:
        print("Seu triâgulo é ISÓSCELES, isso acontece pois dois dos lados são iguais!")
    else:
        print("Seu triângulo é ESCALENO, isso acontece pois todos os lados são diferentes!")
else:
    print("Ele não poderá formar um trinângulo")
