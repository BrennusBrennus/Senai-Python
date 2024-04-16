"""
crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' nou não
"""

nome = input('Nome: ').strip().title().split()
# print('Você tem Silva no nome?', 'Silva' in nome)
# ou:
print(nome)
print('Você tem Silva no nome?', 'Silva' in nome)
