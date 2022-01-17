preço = float(input('Digite o preço para ver o preço com desconto '))
des = preço - (preço * 5 / 100)
print('O preço do produto com 5 porcento de desconto é R$ {:.2f}'.format(des))
