#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaço.
# Ex. apos a sopa / a sacada da casa / o lobo ama o bolo.

palavra: str = (input("Digite sua palavra sem espaços: "))
inverso = (palavra[::-1])
palavra = ''.join(palavra.split())
inverso = ''.join(inverso.split())
if palavra == inverso:
    print("A palavra {} é um  palindromo pois ao inverter fica {}.".format(palavra, inverso))
else:
    print("A palavra {} não forma um palindromo.".format(palavra))
