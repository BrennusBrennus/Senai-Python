import os

os.system('cls || clear')

maiorNumero = -99999999.0
menorNumero = 99999999.0
a: float
b: float

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

if a > maiorNumero: maiorNumero = a
if a < menorNumero: menorNumero = a

if b > maiorNumero: maiorNumero = b
if b < menorNumero: menorNumero = b

print(f'Soma: {a+b}')
print(f'media: {(a+b)/2}')
print(f'Produto: {a*b}')
print(f'Maior: {maiorNumero}')
print(f'Menor: {menorNumero}')