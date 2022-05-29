#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e qnt de dias pelos quais foi usado. com R$60/dia e R$0.15km rodado.
d = int(input('Quantos dias alugados?' ))
km = float(input('Quantos Km rodados?' ))
print('O total a pagar é de R${:.2f}'.format((d*60)+(km*0.15)))
