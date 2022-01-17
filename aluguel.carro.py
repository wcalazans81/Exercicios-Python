dia = int(input('Quantos dias o veículo está alugado? '))
km = float(input('Quantos Km foram rodados? '))
valor = (dia * 60) + (km * 0.15)
print('O valor a pagar pelo aluguel do veículo é de R$ {:.2f}'.format(valor))
