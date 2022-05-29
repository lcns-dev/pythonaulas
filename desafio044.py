# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento.
# À vista dinheiro/cheque 10% de desconto
# À vista no cartão: 5% de desconto.
# em até 2x no cartão preço normal.
# 3x ou mais no cartão: 20% de juros.

print("-=-" * 8)
print("LOJA DO CAMACHO")
print("-=-" * 8)
valor = float(input("Qual o valor do produto? "))
print('''Qual a forma de pagamento?
[ 1 ] À vista no dinheiro ou cheque (10% de desconto).
[ 2 ] À vista no cartão (5% de desconto).
[ 3 ] 2x no cartão de crédito.
[ 4 ] 3x ou mais no cartão (20% de juros)''')
escolha = int(input("Sua escolha: "))
if escolha == 1:
    print("Para o produto no valor de R${:.2f}, pagando á vista, terá 10% de desconto e o valor ficará R${:.2f}".format(valor, (valor - (valor * 10) / 100)))
elif escolha == 2:
    print("Para o produto no valor de R${:.2f}, pagando á vista no cartão, terá 5% de desconto e o valor ficará R${:.2f}".format(valor, (valor - (valor * 5) / 100)))
elif escolha == 3:
    print("Para o produto no valor de R${:.2f}, pagando em 2x no cartão, com duas parcelas de R${:.2f}.".format(valor, valor / 2))
elif escolha == 4:
    parcela = int(input("Quantas parcelas? "))
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(parcela, (valor + (valor * 20 / 100)) / parcela))
    print("Sua compra de R${:.2f} custará no total R${:.2f}.".format(valor, (valor + (valor *20 / 100))))
else:
    print("Opção inválida.")
print("Boas compras !")