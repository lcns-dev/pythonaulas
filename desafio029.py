#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima limite.

import random
vel = random.randint(1, 160)
multa = float(vel * 7)-(7 * 80)
if vel <80:
    print("{}Km/h é uma velocidade permitida.".format(vel))
else:
    print("O limite é 80Km/h, você passou a {}Km/h e foi multado em R${:.2f}.".format(vel, multa))
