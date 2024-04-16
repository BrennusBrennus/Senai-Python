import os
os.system('cls || clear')

soma = 0

for i in range(5):
    soma += int(input(f'Digite o {i+1}º valor: '))
    
print(soma)