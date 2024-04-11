import os
os.system('cls || clear')

nome_produto = input('Produto: ')
quantidade = int(input('Quantidade: '))
preco_unitario = float(input('Preço unitário: R$'))

valor_total = quantidade * preco_unitario

if quantidade <= 5:
    valor_final = valor_total * 0.02
elif quantidade > 5 and quantidade <= 10:
    valor_final = valor_total * 0.03
else:
    valor_final = valor_total * 0.05

print(f'Produto: {nome_produto}')
print(f'Quantidade: {quantidade}')
print(f'Preço antes do reajuste: R${valor_total:.2f}')
print(f'Preço após o reajuste: R${valor_final:.2f}')




