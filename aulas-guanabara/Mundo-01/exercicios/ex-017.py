"""
crie um programa que leia o comprimemto do cateto oposto e do cateto adjacente de um trângulo retângulo
e ca calcule o comprimento da hipotenusa
"""

import math

cateto_oposto = float(input('Valor do cateto oposto: '))
cateto_adjacente = float(input('Valor do cateto adjacente: '))

# hipotenusa = math.sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
hipotenusa = (cateto_adjacente ** 2 + cateto_oposto ** 2) ** (1/2)

print(f'Valor da hipotenusa: {hipotenusa}\n')

print(  '                 *')
print(  '                 * **')
print(  '                 *   ***')
print( f'                 *      ***  {hipotenusa}m²')
print( f'          {cateto_oposto}m²  *          ***')
print(  '                 *            ***')
print(  '                 *               ***')
print(  '                 *                  ***')
print(  '                 *************************')
print(f'                            {cateto_adjacente}m²')
