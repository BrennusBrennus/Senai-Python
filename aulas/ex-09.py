import os
os.system('cls || clear')

print('               Até 5Kg            Acima de 5Kg')
print('Morango    R$ 2,50 por Kg        R$ 2,20 por Kg')
print('Maçã       R$ 1,80 por Kg        R$ 1,50 por Kg')
print('-----------------------------------------------')
quilos_morango = float(input('Quantos quilos de morango você deseja comprar? '))
if quilos_morango <= 5:
    preco_total_morango = quilos_morango * 2.5
else:
    preco_total_morango = quilos_morango * 2.2

quilos_maca = float(input('Quantos quilos de maçã você deseja comprar? '))
if quilos_maca <= 5:
    preco_total_maca = quilos_maca * 1.8
else:
    preco_total_maca = quilos_maca * 1.5


quilo_total = quilos_morango + quilos_maca
preco_total = preco_total_morango + preco_total_maca

if quilo_total > 8 or preco_total > 25:
    preco_total = preco_total * 0.10

print(f'Valor total a ser pago: R${preco_total:.2f}')