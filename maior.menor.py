from time import sleep
a = int(input   ('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))
print('\033[31mPROCESSANDO....\033[m')
sleep(3)

# Verificando quem é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi \033[33m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[32m{}\033[m'.format(maior))