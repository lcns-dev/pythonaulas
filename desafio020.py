#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a tela ordem sorteada.
import random
print('Olá Professor tudo bem? Quais os nomes dos alunos que iram apresentar?')
al1 = str(input('Qual o nome do 1° aluno? '))
al2 = str(input('Qual o nome do 2° aluno? '))
al3 = str(input('Qual o nome do 3° aluno? '))
al4 = str(input('Qual o nome do 4° aluno? '))
lista = [al1,al2,al3,al4]
random.shuffle(lista)
print('Entre os alunos: {}, {}, {} e {}.'.format(al1, al2, al3, al4))
print('A sequência para a apresentação dos trabalhos será: ')
print(lista)


