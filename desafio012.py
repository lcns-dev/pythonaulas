# Faça um algoritmo que leia o preço de um produto e mostre sue novo preço, com 5% de desconto e parcelado terá 8% de aumento.
n = float(input('Qual o valor do produto? R$'))
print('Na liquidação este produto de R${:.2f}'.format(n))
print('À vista o produto terá R${:.2f} de desconto e sairá por R${:.2f} '.format((n*5)/100, (n-(n*5)/100)))
print('A prazo o produto terá R${:.2f} valor será de R${:.2f}'.format((n*8)/100, (n+(n*8)/100)))
