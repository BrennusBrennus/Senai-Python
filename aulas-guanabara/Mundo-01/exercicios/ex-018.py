"""
crie um programa que leia um ângulo qualquer e retorne o valor do seno, do cosseno e da tangente
"""

import math

angle = float(input('Ângulo: '))


sin = math.cos(math.radians(angle))
cos = math.sin(math.radians(angle))
tan = math.tan(math.radians(angle))

print(f'Seno: {sin:.2f}')
print(f'Cosseno: {cos:.2f}')
print(f'Tangente: {tan:.2f}')
