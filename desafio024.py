#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
cidade = input("Qual o nome da sua cidade? ")
santo = cidade.title()
print("Santo" in santo)