# Crie um programa para aprovar o empréstimo bancário para a comprea de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da preatação mensal, sabendo que ela não pode exceder 30% da salário ou então o empréstimo será negado.

vi = float(input("Qual o valor do imóvel? R$"))
sal = float(input("Qual sua renda? R$"))
ano = int(input("Em quantos anos para o financiamento? ")) * 12
prest = vi / (ano)
if prest > (sal * 30) / 100:
    print("Empréstimo \033[4;31mNEGADO!!!\033[m Para uma casa no valor de R${:.2f} o valor da parcela de R${:.2f} excede os 30% do salário.".format(vi, prest))
else:
    print("Parabéns, empréstimo \033[4;32mCONCEDIDO!\033[m Para o imóvel de R${:.2f} a prestação será de {:.2f}!!!".format(vi, prest))
