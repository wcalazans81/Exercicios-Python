import random
n = str(input('Nome do 1º aluno: '))
n1 = str(input('Nome do 2º aluno: '))
n2 = str(input('Nome do 3º aluno: '))
n3 = str(input('Nome do 4º aluno: '))
lista = [n, n1, n2, n3]
# choice escolhe um str
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
