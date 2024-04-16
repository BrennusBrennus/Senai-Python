import os
os.system('cls || clear')

cont = 0
soma = 0
i: int

for i in range(2):
    # nota = -1
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    while nota < 0 or nota > 10:
        nota = float(input(f'Digite a {i + 1}ª nota: '))
    soma += nota
    cont += 1
    nota = 0
    os.system('cls || clear')

print(f'Média: {soma/cont:.2f}')
