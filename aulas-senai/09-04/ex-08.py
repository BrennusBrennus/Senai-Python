import os
os.system('cls || clear')

tipo_operacao = input('Escolha a operação a ser realizada (+, -, *, /): ')
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

if tipo_operacao == '+':
    operacao = a + b
elif tipo_operacao == '-':
    operacao = a - b
elif tipo_operacao == '*':
    operacao = a * b
elif tipo_operacao == '/':
    operacao = a / b

print(f'{a} {tipo_operacao} {b} = {operacao}')




