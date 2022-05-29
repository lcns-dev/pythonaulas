# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para Binário. / 2 para octal. / 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:")
[ 1 ] converter para BINÁRIO")
[ 2 ] converter para OCTAL")
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input("Sua escolha: "))
if escolha == 1:
    print("O número {} em BINÁRIO fica: {}".format(num, bin(num)[2:]))
elif escolha == 2:
    print("O número {} em OCTAL fica: {}".format(num, oct(num)[2:]))
elif escolha == 3:
    print("O número {} em HEXADECIMAL fica: {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida !")