# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artífico, indo de 10 até 0, com pausa de 1seg entre eles.
import time

print("Contagem regrassiva para o estouro dos fogos!!!")
for contagem in range(10, -1, -1):
    time.sleep(1)
    print(contagem)
print("FIM !!!")