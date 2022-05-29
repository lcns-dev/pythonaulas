# Façã um programa que leia 3 número e diga qual é o maior e o menor.
n1 = int(input("Escolha o 1º número: "))
n2 = int(input("Escolha o 2º número: "))
n3 = int(input("Escolha o 3º número: "))
if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número.")
elif n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número.")
if n2 < n1 and n1 < n3:
    print(f"{n2} é o menor número.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número.")
if n3 < n1 and n3 < n2:
    print(f"{n3} é o menor número.")
elif n3 > n1 and n3 > n2:
    print(f"{n3} é o maior número.")
