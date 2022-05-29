#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = "F" or "M"
while sexo != "F" or "M":
    sexo = str(input("Digite o sexo: ")).upper()
    if sexo == "M" or sexo == "F":
        print("Pronto registrado.")
        print("Fim!")
    else:
        print("Digite um valor válido [M/F] !")
print("FIM!")
