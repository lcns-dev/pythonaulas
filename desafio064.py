#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (DESCONCIDERANDO O FLAG)

print("Vamos somar seus número REAIS? Comece agora!")
num =[]
while True:
    lista = int(input(("Digite um número: (999 se acabou)")))
    if lista == 999:
        break
    num.append(lista)
for i in num:
    menor = (min(num))
    maior = (max(num))
    soma = (sum(num))
    count = len(num)
print("Foram digitados {} número sendo: O menor número foi {}, O maior número foi {} e a soma deles foi {}".format(count, menor, maior, soma))