import os
os.system('cls || clear')

soma = 0
cont = 0

resp = input('Deseja inserir uma nota? (s / n) ').upper().strip()
if resp == 'N':
    print('Encerrando o programa...')
else:
    while resp != 'N':
        nota = float(input('Digite uma nota: '))
        soma += nota
        cont += 1
        nota = 0
        resp = input('Deseja outra nota? (s / n) ').upper().strip()

media = soma / cont

print(f'Média: {media:.2f}')
print(f'Quantidade de loops: {cont}')