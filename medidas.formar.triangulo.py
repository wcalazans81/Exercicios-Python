print('\033[36m<=>\033[m'*20)
print('Analizador de Triângulos')
print('\033[35mo=o\033[m'*20)
r1 = float(input('1º segmento de reta: '))
r2 = float(input('2º segmento de reta: '))
r3 = float(input('3º segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima POODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')