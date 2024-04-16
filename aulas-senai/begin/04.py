import os

os.system('cls || clear')

nota1: float
nota2: float
nota3: float
nota4: float
media: float
nome: str
idade: int

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'{nome}, a sua média é {media}')

