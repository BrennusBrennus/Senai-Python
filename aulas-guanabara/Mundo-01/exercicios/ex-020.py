"""
crie um programa que leie 4 nomes e diga a ordem de apresentação
"""

from random import shuffle

nome_um = input('primeiro nome: ')
nome_dois = input('segundo nome: ')
nome_tres = input('terceiro nome: ')
nome_quatro = input('quarto nome: ')

lista = [nome_um, nome_dois, nome_tres, nome_quatro]

ordem = shuffle(lista)

print(f'A ordem de apresentação é: {lista}')