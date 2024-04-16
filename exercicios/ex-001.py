import os
os.system('cls || clear')

soma = 0

for i in range(5):
    if i == 0:
        soma += int(input('Digite um valor: '))
    else:
        soma += int(input('Digite outro valor: '))

print(soma)