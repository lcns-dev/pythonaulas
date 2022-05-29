# Desenvolva um programa que leia o nome idade e sexo de 4 pessoas.
# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

nome = []
idade = []
sexo = []
pessoas = []
velho: str = " "
maioridade = 0
for c in range(1, 5):
    print("----- {}ª PESSOA -----".format(c))
    nome.append(str(input("Nome: ".strip())))
    idade.append(int(input("Idade: ")))
    sexo.append(str(input("Sexo [M/F]:".upper())))
    if c == 1 and sexo in "Mm":
        maioridade = idade
        velho = nome
    if sexo in "Mm" and idade > maioridade:
        maioridade = idade
        velho = nome

print("A média de idade do grupo de {} pessoas é de {:.1f} anos".format(c, (sum(idade) / c)))
print("O homem mais velho tem {} anos e se chama {}".format(maioridade, velho))