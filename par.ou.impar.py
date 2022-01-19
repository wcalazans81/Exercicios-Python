num = int(input('Digite qualquer número para saber se o número é PAR ou IMPAR: '))
if num % 2 == 0:
    print('Você digitou o número \033[33m{}\033[m e ele é um número \033[34mPAR\033[m!!!'.format(num))
else:
    print('Você digitou o número \033[33m{}\033[m e ele é um número \033[34mIMPAR\033[m!!!'.format(num))
