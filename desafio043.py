# Desenvolve uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: Abaixo do peso.
# entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40 obesidade.
# acima de 40: obesidade mórbida.

peso = float(input("Qual o seu peso? (Kg)"))
altura = float(input("Qual sua altura? "))
imc = peso / altura ** 2
if imc < 18.5:
    print("Com {}Kg e {}m de altura seu IMC é {:.2f}.".format(peso, altura, imc))
    print("ABAIXO DO PESO !!!")
elif imc > 18.5 and imc < 25:
    print("Com {}Kg e {}m de altura seu IMC é {:.2f}.".format(peso, altura, imc))
    print("PESO IDEAL !!!")
elif imc > 25 and imc < 30:
    print("Com {}Kg e {}m de altura seu IMC é {:.2f}".format(peso, altura, imc))
    print("SOBREPESO !!!")
elif imc > 30 and imc < 40:
    print("Com {}Kg e {}m de altura seu IMC é {:.2f}".format(peso, altura, imc))
    print("OBESIDADE !!!")
else:
    print("Com {}Kg e {}m de altura seu IMC é {:.2f}".format(peso, altura, imc))
    print("OBESIDADE MÓRBIDA !!!")