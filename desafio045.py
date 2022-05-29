# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print("*" * 20)
print("Jogo do Jokenpô")
print("*" * 20)
print("Escolha entre: Papel, Pedra, Tesoura")
escolha = (input("Qual sua escolha? ").title())
pc = random.choice(["Tesoura", "Papel", "Pedra"])
if escolha == "Papel" and pc == "Pedra":
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("PARABÉNS, você ganhou !!!")
elif escolha == "Papel" and pc == "Tesoura":
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("Eu GANHEI de você humano !!!")
elif escolha == "Pedra" and pc == "Papel":
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("Eu GANHEI de você humano !!!")
elif escolha == "Pedra" and pc == "Tesoura":
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("PARABÉNS, você ganhou !!!")
elif escolha == "Tesoura" and pc == "Pedra":
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("Eu GANHEI de você humano.")
elif escolha == "Tesoura" and pc == "Papel":
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("PARABÉNS, você ganhou !!!")
elif escolha == pc:
    print("Você escolheu {} e eu escolhi {}.".format(escolha, pc))
    print("Empatamos")
else:
    print("Opção inválida!")