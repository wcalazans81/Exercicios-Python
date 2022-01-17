n = float(input('Digite o valor em reais para conversão R$ '))
l = n / 7.57
e = n / 6.32
d = n / 5.53
p = n / 0.053
print('Com R$ {:.2f} você pode comprar L$ {:.2f} Libras esterlina'.format(n, l))
print('E${:.2f}Euros {:.2f} Dolares$ Peso Agentino${:.2f}'.format(e, d, p))
