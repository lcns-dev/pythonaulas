#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares, ienes, euros e libras esterlinas ela pode comprar!
n = float(input('Quanto dinhiro você tem? R$'))
print('Sabia que com o valor de R${:.2f}, você pode:\nComprar US${:.2f}\nComprar ¥{:.2f}\nComprar €{:.2f}\nComprar £{:.2f}'.format(n, n/5.06, n/0.044, n/5.52, n/6.63))
