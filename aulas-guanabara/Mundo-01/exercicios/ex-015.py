"""
crie um programa que leia a quantidade e Km rodados e os dias alugados.
Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 15 centavos
por Km rodado.
"""

valorKm = 0.15
valorCarro = 60

print('=== Aluguel de Carros ===')
dias = int(input('Dias alugados: '))
km_rodados = float(input('Km rodados: '))

valor_dias_carro = valorCarro * dias
valor_km_rodados = km_rodados * valorKm

valor_total = valor_km_rodados + valor_dias_carro

print(f'Valor total a pagar: R$ {valor_total:.2f}')

print('\nForma simplificada')
valor_total = (dias * 60) + (km_rodados * 0.15)
print(f'Valor total a pagar: R$ {valor_total:.2f}')
