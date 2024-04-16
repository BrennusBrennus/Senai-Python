import os
os.system('cls || clear')

frase1 = 'Estou estudando Python'

print(frase1[16:])

for i in range(22):
    print(frase1[i], end=' - ')

print('\n')
for j in range(22):
    # upper = tranforma um texto em caixa baixa para caixa alta
    print(str.upper(frase1[j]), end=' ')

print('\n')
for k in range(22):
    # transforma um texto em caixa alta para caixa baixa
    print(str.lower(frase1[k]), end=' ')

print('\n')
# : = serve para indicar a posição desejada para a impressão da sua string
print(frase1[0::3])

print(len(frase1))

# count = conta quantas vezes determinado caractere ou texto aparece numa string
# count('',0,13)
print(frase1.count('o', 0, 15))

# find = retorna a posição do índice em que dterminado texto começa numa string
print(frase1.find(' '))

# 'texto' in <variavel> = Lê o texto e retorna True ou False caso ele esteja presente ou não
print('Estou' in frase1)

# replace = substitui determinado texto por outro
palavra = 'arroz cozido'
print(palavra.replace('r', 'm'))
print(palavra.replace('cozido', 'triturado'))

# capitalize = transforma apenas o primeiro caractere de uma string em maiuscula
frase2 = 'breno henrique'
print(frase2.capitalize())

# title = transforma em uppercase o primeiro caractere de cada palavra dentro de uma string
print(frase2.title())

# swapcase = converte caracteres lower para upper e upper para lower
frase3 = 'Laura Vitoria'
print(frase3.swapcase())

# strip = remove os espaços presentes no começo e no final de cada string
frase4 = '   Breno e Laura   '
print(frase4)
print(str.strip(frase4))

# lstrip = remove os espaços presentes no começo de uma string (à esquerda)
# rstrip = remove os espaços presentes no final de uma string (à direita)
print(frase4.lstrip())
print(frase4.rstrip())

"""
split = divide uma string em uma lista onde cada palavra separada é um item da mesma.
Por padrão, o separador é o espaço entre as palavras, mas você pode alterá-lo
"""
frase5 = 'Breno Henrique Gomes do Nascimento'
print(frase5)
print(frase5.split())

# join = une os textos separados de uma lista através de um iterador escolhido por você
frase6 = {'Breno', 'Henrique', 'Gomes', 'do', 'Nascimento'}
print('-'.join(frase6))






