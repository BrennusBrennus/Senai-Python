# crie um programa que leia quanto dinheiro ela tem na carteira e diga quantos dólares ela pode comprar

dolar = 5.12

print('Quantos reais você tem na carteira?')
valor = float(input('R$ '))

dolaresComprados = valor / dolar

print(f'Você pode comprar U$ {dolaresComprados:.2f}')

