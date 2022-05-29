# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atigida.
# Média abaixo de 5.0: REPROVADO. / Média entre 5.0 e 6.9: RECUPERAÇÃO / Média 7.0 ou superior: APROVADO.
n1 = float(input("Nota do 1º semestre: "))
n2 = float(input("Nota do 2º semestre: "))
media = (n1 + n2) / 2
if media < 5:
    print("REPROVADO! Com notas entre {:.2f} e {:.2f} tem média {:.2f}.".format(n1, n2, media))
elif media == 5 or media < 6.9:
    print("RECUPERAÇÃO! Com notas entre {:.2f} e {:.2f} tem média {:.2f}.".format(n1, n2, media))
else:
    print("APROVADO! Com notas entre {:.2f} e {:.2f} tem a média {:.2f}.".format(n1, n2, media))
