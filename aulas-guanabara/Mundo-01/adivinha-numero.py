import random

"""
num = random.randint(1, 10)

while True:
    resp = int(input('Digite um número: '))
    if resp < num:
        print('É maior')
    elif resp > num:
        print('É menor')
    if resp == num:
        break

print(f'Acertou: {num}')
"""

num1 = int(input('Começo: '))
num2 = int(input('Fim: '))

valor = random.randint(num1, num2)

while True:
    resp = int(input('Digite um número: '))
    if resp < valor:
        print('É maior')
    elif resp > valor:
        print('É menor')
    if resp == valor:
        break

print(f'Acertou: {valor}')
