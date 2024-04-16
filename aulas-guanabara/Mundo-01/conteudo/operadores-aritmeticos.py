# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % resto da divisão

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)

"""
    ordem de precedência
    
    primeiro lugar: ()
    segundo lugar: **
    terceiro lugar: *, /, //, %
    quarto lugar: +, - 
"""

print(5+3*2)
print(2**(5-2)+4/2*6-10)
print(354**535)

nome = input('nome: ')
print(f'prazer, {nome:=^20}!')  # pode-se usar também {:>20}, {:<20}, {:^20}

print('testando a locação')
print('de textos')

print('testando a locação', end=' ')
print('de textos')

print('realizando \nmais um teste')

