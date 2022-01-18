frase = 'Curso em Vídeo Python'
parte_da_Frase = frase.split()
# função len() mostra a quantidade de caracteres de um lista
print('Esta frase tem {} caracteres'.format(len(frase)))
# função count() conta quantos caracteres tem a str ou pode contar um ou mais letras em especifico
print('Esta frase tem {} ltras o'.format(frase.count('o')))
# função strip() remove os esspaços no inicio e no final da frase ou str
print(frase.strip())
# funcão replace() troca um palavra por outra
print(frase.replace('Python', 'Android'))
# função find() mostra a posição da letra ou palavra na cadeia de caracteres 
# obs: se retornar -1 não encontrou a palavra
print('A palavra Vídeo inicia-se na posiçao {}'.format(frase.find('Vídeo')))
# função split() separa a str ou frase em sublistas sepparando no espaço entre palavras
print(frase.split())
# para motrar partes de um frase splitada é necessário jogar o split dentro de uma variável
print('A parte da frase que está na posição splitada 2 é {:=^20}'.format(parte_da_Frase[2]))
# para fazer um verificação logica para ver se um determinado elemento está dentro da str
print('A palavra Curso esta na frase {}'.format('Curso' in frase))
# escreva a frase
print(frase)
# fatiar str para mostrar um letra obs: sempre comece a contar do 0
print(frase[3])
# fatiar str começando de um ponto na str até outro ponto obs:sempre desconsidere o ultimo se é de 9 a 13 desconsidere o 13
print(frase[9:13])
# do inicio até o final da str print(frase[:13]), do final para o inicio print(frase[13:])
print(frase[:13], frase[12:])
# saltando de 2 em 2
print(frase[:13:2])
# print para escrever textos grandes use print("""texto""")
