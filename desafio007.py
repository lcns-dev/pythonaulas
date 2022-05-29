# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = input('Qual o nome do aluno? ')
n1 = float(input('Nota do 1º semestre (1 a 10): '))
n2 = float(input('Nota do 2º semestre (1 a 10): '))
print('A média entre {} e {} do aluno {} é igual a: {:.1f}'.format(n1, n2, nome, (n1+n2)/2))
