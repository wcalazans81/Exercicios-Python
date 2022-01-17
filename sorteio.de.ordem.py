import random
n = str(input('Nome do 1º aluno: '))
n1 = str(input('Nome do 2º aluno: '))
n2 = str(input('Nome do 3º aluno: '))
n3 = str(input('Nome do 4º aluno: '))
lista = [n, n1, n2, n3]
# O metodo shuffle e embaralhar
random.shuffle(lista)
print('A ordem de apresentação do trabalho de física será')
print(lista)