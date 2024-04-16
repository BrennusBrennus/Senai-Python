"""
crie um programa que leia a altura e a largura e retorne a área em metros quadrados
além disso, diga quantas latas de tinta serão necessárias para pintar essa parede
lembrando que uma lata pinta uma área de 2m²
"""

altura = float(input('Altura: '))
largura = float(input('Largura: '))

area = altura * largura
litros = area / 2

print(f'Área: {area:.1f}m²')
print(f'Litros de tinta necessários: {litros:.1f}')
