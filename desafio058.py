#Melhore o jogo do Desafio 028 onde o computador vai pensar em um número de 0 até 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram foram necessários para vencer.

import random
print("-=" * 30)
print("Vou pensar em um número de 0 até 10, tente adivinhar.")
print("-=" * 30)
pc = int(input("Em que número eu pensei?"))
num = random.randint(0, 10)
cont = 0
while pc == num:
    print("")