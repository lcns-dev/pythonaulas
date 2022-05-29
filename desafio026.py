#Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A".
# 2. Em que posição ela aparece o primeira vez.
# 3. Em que posição ela aparece a última vez.
frase = str(input("Digite uma frase: ")).strip().lower()
primeira = frase.find('a')
print("A letra 'a' aparece {} vezes na frase. ".format(frase.lower().count('a')))
print("Ele inicia no {}º caractere.".format((primeira)+1))
print("Ele aparece a última vez no {}º caractere.".format(frase.rfind('a')+1))