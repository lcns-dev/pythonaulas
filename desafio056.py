# Desenvolva um programa que leia o nome idade e sexo de 4 pessoas.
# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaidade = 0
médiaidade = 0
homemvelho = 0
nomevelho = " "
totmulher = 0
for p in range(1, 5):
    print("----- {}ª pessoa -----".format(p))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] "))
    somaidade += idade
    if p == 1 and sexo in "Mm":
        homemvelho = idade
        nomevelho = nome
    if sexo in "Mm" and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher =+ 1
médiaidade = somaidade / 4
print("A média de idades do grupo é {:.1f} anos.".format(médiaidade))
print("O nome do homem mais velho é {} com {} anos.".format(nomevelho, homemvelho))
print("Existem {} mulheres com menos de 20 anos.".format(totmulher))
