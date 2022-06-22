#Melhore o jogo do Desafio 028 onde o computador vai pensar em um número de 0 até 10.
# Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram foram necessários para vencer.

from random import randint
print("-=" * 30)
print("Vou pensar em um número de 0 até 10, tente adivinhar.")
print("-=" * 30)
pc = randint(0, 10)
cont = 0
acertou = False
while not acertou:
    escolha = int(input("Em que número eu pensei?"))
    if pc == escolha:
        acertou = True
    else:
        print("ERROU!!! Tente outra vez!")
print("ACERTOU!!!")
