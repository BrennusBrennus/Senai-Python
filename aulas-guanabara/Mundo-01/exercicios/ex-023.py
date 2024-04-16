"""
crie um programa que leia um número de 0 a 9999 e mosrte na tela os dígitos separados.
Ex: 2024
unidade = 4
dezena = 2
centena = 0
milhar = 2
"""
a = str(input('Digite um número: '))
b = int(a)

unidade = b // 1 % 10
dezena = b // 10 % 10
centena = b // 100 % 10
milhar = b // 1000 % 10
"""
print('Unidade: ', a[3])
print('Dezena: ', a[2])
print('Centena: ', a[1])
print('Milhar: : ', a[0])
"""

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')



