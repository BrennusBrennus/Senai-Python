# crie um programa que leia um valor em celsius e o converta para fahrenheit

print('=== Conversor de Celsius para Fahrenheit')
celsius = float(input('ºC: '))

fahrenheit = celsius * 1.8 + 32

print(f'ºF: {fahrenheit:.2f}')