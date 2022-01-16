# Ordem de precedência dos operadores aritméticos
# 1ª ()
# 2ª ** potênciação
# 3ª * multiplicação, / divisão, // divisão inteira, % resto da divisão 
# 4ª + soma, - subitrasão, **(1/2) raiz quadrada
n = int(input('Digite um valor '))
n1 = int(input('Digite outro valor ')) 
soma = n + n1
subitracao = n - n1
mult = n * n1
div = n / n1
divint = n // n1
restodiv = n % n1
raiz = (n + n1) **(1/2) 
print('A soma é {} e a subtração é {} e a multiplicação é {}'.format(soma, subitracao, mult))
print('A divisão é {:.2f} e a divisão inteira é {} e o resto da divisão é {}'.format(div, divint, restodiv), end=' ')
print('E a raiz quadrada de {} + {} = {:.2f}'.format(n, n1, raiz))