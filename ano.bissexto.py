from datetime import date
from time import sleep
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
sleep(3)
print('\034[31mPOCESSANDO...\033[m')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é BISSEXTO!\033[m'.format(ano))
else:
    print('\033[31mO ano {} não é BISSEXTO!\033[m'.format(ano)) 