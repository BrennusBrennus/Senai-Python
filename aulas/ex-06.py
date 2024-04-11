import os
os.system('clear || cls')

par = 0
impar = 0
soma = 0

numero_um = int(input('Digite o primeiro número: '))
soma += numero_um
if numero_um % 2 == 0:
    par += 1
else:
    impar += 1

numero_dois = int(input('Digite o segundo número: '))
soma += numero_dois
if numero_dois % 2 == 0:
    par += 1
else:
    impar += 1

numero_tres = int(input('Digite o terceiro número: '))
soma += numero_tres
if numero_tres % 2 == 0:
    par += 1
else:
    impar += 1
numero_quatro = int(input('Digite o quarto número: '))
soma += numero_quatro
if numero_quatro % 2 == 0:
    par += 1
else:
    impar += 1
    
numero_cinco = int(input('Digite o quinto número: '))
soma += numero_cinco
if numero_cinco % 2 == 0:
    par += 1
else:
    impar += 1

#soma = numero_cinco + numero_quatro + numero_tres + numero_dois + numero_um

print(f'Soma: {soma}')
print(f'Quantidade de pares: {par}')
print(f'Quantidade de ímpares: {impar}')
