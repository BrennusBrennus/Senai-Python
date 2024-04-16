# crie um algoritmo que leia o preço de um produto e mostre o preço com 5% de desconto

valorProduto = float(input('Valor do produto: R$ '))
valorDescontado = valorProduto * 5 / 100
valorReajustado = valorProduto - valorDescontado

print(f'Valor com reajuste: R$ {valorReajustado:.2f}')
print(f'Valor descontado: R$ {valorDescontado:.2f}')