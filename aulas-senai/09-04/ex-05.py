import os
os.system('cls || clear')

num = int(input('Digite a sua idade: '))
if num < 18 or num > 65:
    print('Não vota')
else:
    print('Vota')