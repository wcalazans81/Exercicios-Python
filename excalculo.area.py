from statistics import quantiles


alt = float(input('Digite a altura da parede em metros '))
larg = float(input('Digite a largura da parede em metros '))
area = alt * larg
quant = area / 2
print('A área da parede é de {:.2f} M²'.format(area))
print('Para pintar a área da parede você vai gastar {:.2f} litros de tinta'.format(quant))
