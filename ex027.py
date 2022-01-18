frase = str(input('Digite um frase:')).strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A 1ª letra a aparece n posição {}'.format(frase.find('a')+1))
print('A úttima letra A apreceu na posição {}'.format(frase.rfind('a')+1))