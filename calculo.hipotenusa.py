#co = float(input('Digite o comprimento do cateto opsto:  '))
#ca = float(input('Digite o comprimento do cateto adjacente: '))
#hi = (co **2 + ca**2) **(1/2)
#print('A hipotenusa vai medir {:.2f} cm'.format(hi))
#import math
#co = float(input('Digite o comprimento do cateto opsto:  '))
#ca = float(input('Digite o comprimento do cateto adjacente: '))
#hi = math.hypot(co, ca)
#print('A hipotenusa vai medir {:.2f} cm'.format(hi))
from math import hypot
co = float(input('Digite o comprimento do cateto opsto:  '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f} cm'.format(hi))