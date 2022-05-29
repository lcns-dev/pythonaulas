#Um professor quer sortear um dos seus quatro alunos para apagar a lousa. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
a1 = input('Qual o primeiro aluno? ')
a2 = input('Qual o segundo aluno? ')
a3 = input('Qual o terceiro aluno? ')
a4 = input('Qual o quarto aluno?')
alunos = [a1,a2,a3,a4]
random.choice(alunos)
print('SORTEIO para limpar o quadro!!!')
print("O escolhido para apagar o nosso quadro, foi o {}. Parabéns e venha já para esse quadro.".format(random.choice(alunos)))
