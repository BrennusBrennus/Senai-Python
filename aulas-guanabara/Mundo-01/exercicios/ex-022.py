"""
crie um programa que leia o nome completo de uma pessoa e imprima na tela:
> o nome com todas as letras maiúsculas;
> o nome com todas as letras minúsculas;
> quantas letras tem no total (desconiderar espaços);
> quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o seu nome: ')).strip()
print(f'Nome com .upper(): {nome.upper()}')
print(f'Nome com .lower(): {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(' ')}')
print(f'Quantidade de letras no primeiro nome: {len(nome.split()[0])}')
# print(f'Quantidade de letras no primeiro nome: {nome.find(' ')}')


