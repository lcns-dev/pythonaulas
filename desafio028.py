# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu.
# Obs. Vamos utilizar neste programa o RANDOM, IF e ELSE.

import random
print("-=" * 40)
print("Vou pensar em um número de 0 até 5. Tente adivinhar...")
print("-=" * 40)
escolha = int(input("Em que número pensei? "))
num = random.randint(0, 5)
if escolha == num:
    print("Parabéns você acertou o número escolhido foi {}.".format(num))
else:
    print("Você errou e eu ganhei, o núemro escolhido foi {}, tente novamente.".format(num))
