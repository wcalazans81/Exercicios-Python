from dataclasses import replace


vel = int(input('Qual é a velocidade atual do veículo?\033[32m '))
print('\033[33m=+=\033[m'*20)
ex = (vel - 80) * 7
if vel <= 80:
    print('Parabéns continue conduzindo seu veículo com segurança')
else:
    print('\033[31mVocê ultrapassou o limite de 80km\033[m')
    print('Você será multado em R$\033[33m{:.2f}\033[m'.format(ex))
