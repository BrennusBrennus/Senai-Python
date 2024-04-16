"""
crie um programa que leia o nome de 4 pessoas e sorteie um deles
"""

import math
from random import choice

nome_um = input('primeiro nome: ')
nome_dois = input('segundo nome: ')
nome_tres = input('terceiro nome: ')
nome_quatro = input('quarto nome: ')

lista_nomes = [nome_um, nome_dois, nome_tres, nome_quatro]
sorteado = choice(lista_nomes)

print(f'nome sorteado: {sorteado}')
