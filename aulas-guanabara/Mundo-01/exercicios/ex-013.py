# crie um algoritmo que leia o saláro de um funcionário e o retorne com 15% de aumento

salario = float(input('Salário atual: R$ '))

valor_aumento = salario * 15 / 100
salarioReajustado = salario + valor_aumento

print(f'Novo salário: R${salarioReajustado:.2f}')
print(f'Valor aumentado: R${valor_aumento:.2f}')