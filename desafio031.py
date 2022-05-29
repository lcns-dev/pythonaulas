# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por para viagens de até 200km e R$0,45 para viagens mais longas.
num = float(input("Qual a distância da viagem em Km? "))
v1 = num * 0.50
v2 = num * 0.45
if num <= 200:
    print("A viagem terá um custo total de R${:.2F}.".format(v1))
else:
    print("A viagem terá um custo total de R${:.2F}".format(v2))
print("BOA VIAGEM!")