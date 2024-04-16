import os
os.system('cls || clear')

cont = 0
soma = 0
i: int
# nota = -1
for i in range(3):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    while nota < 0 or nota > 10:
        nota = float(input(f'Digite a {i + 1}ª nota: '))
    soma += nota
    cont += 1
    nota = 0
    os.system('cls || clear')

print(f'Média: {soma/cont:.2f}')

if soma/cont >= 7:
    print('Aluno APROVADO')
elif soma/cont >= 5:
    print('Aluno EM RECUPERAÇÂO')
else:  
    print('Aluno REPROVADO')


