from random import choice

n1 = input("Digite o nome do primeiro aluno: \n")
n2 = input("Digite o nome do segundo aluno: \n")
n3 = input("Digite o nome do terceiro aluno: \n")
n4 = input("Digite o nome do quarto aluno: \n")

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print ("O aluno escolhido foi {}".format(escolhido))
