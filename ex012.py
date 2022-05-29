#Estrutura condicional aninhada.
nome = str(input("Qual o seu nome? "))
if nome == "Leandro":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print("Seu nome é bem comum no Brasil.")
else:
    print("Seu nome é bem normal!")
print("Tenha um bom dia {}".format(nome))
