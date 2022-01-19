from random import randint
from time import sleep
cor = {31 : '\033[31m', 32 : '\033[32m', 33 : '\033[33m', 34 : '\033[34m', 'f' : '\033[m'}
n = randint(1, 10)
print(cor[33], '=*=+=*='*14, cor['f'])
print('Tente adivinhar o número {}entre 0 a 10 {}escolhido pelo computador e vença o jogo '.format(cor[31], cor['f']))
print(cor[33], '=*=+=*='*14, cor['f'])
jog = int(input('Escolha seu número te tente vencer: '))
print(cor[31],'PROCESSANDO....',cor['f'])
sleep(3)
if n == jog:
    print(cor[32], '=0='*30, cor['f'])
    print('O computador escolheu o Nº {}{}{} e você o Nº {}{}{} PARABENS VOCÊ VENCEU!!!'.format(cor[31], n,cor['f'],cor[33], jog,cor['f']))
else:
    print('O computador escolheu o Nº {}{}{} e você o Nº {}{}{} Você é muito pato PERDEU TENTE NOVAMENTE!!!'.format(cor[31], n,cor['f'],cor[33], jog,cor['f']))