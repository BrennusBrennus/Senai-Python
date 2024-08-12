from os import system
from time import sleep


def pagamento(subtotal, diferenca, cod, nome_pagamento):
    total = 0
    if cod == 1:
        total = subtotal + diferenca
    else:
        total = subtotal - diferenca

    system('cls || clear')
    print('Pratos Escolhidos')
    for i in pratos:
        print(f'• {i}')
    print('-----------------------------------')
    print(f'Forma de pagamento: {nome_pagamento}')
    print(f'Subtotal: R$ {subtotal:.2f}')
    print(f'Diferença:{diferenca:.2f}')
    print(f'Total: {total:.2f}')
    exit()


def forma_pagamento():
    print('----------------------')
    print('| código | descrição |')
    print('|--------------------|')
    print('|   1    |  CARTÃO   |')
    print('|   2    | DINHEIRO  |')
    cod = int(input('----------------------\n'))
    while cod < 1 or cod > 2:
        cod = int(input('Opção inválida! Digite o código\n'))

    f_pagamento = ''
    if cod == 1:
        f_pagamento = 'Cartão'
    else:
        f_pagamento = 'Dinheiro'

    subtotal = 0
    for i in range(len(valor_pratos)):
        subtotal += valor_pratos[i]

    diferenca = subtotal * 0.1

    pagamento(subtotal, diferenca, cod, f_pagamento)


pratos = []
valor_pratos = []


def valida_codigo(codigo):

    valor_prato = 0
    match codigo:
        case 1:
            prato = 'código 1 - Lasanha'
            pratos.append(prato)
            valor_prato = 40.0
            valor_pratos.append(valor_prato)
        case 2:
            prato = 'código 2 - Feijoada'
            pratos.append(prato)
            valor_prato = 40.0
            valor_pratos.append(valor_prato)
        case 3:
            prato = 'código 3 - Strogonoff'
            pratos.append(prato)
            valor_prato = 37.0
            valor_pratos.append(valor_prato)
        case 4:
            prato = 'código 4 - Mocotó'
            pratos.append(prato)
            valor_prato = 25.0
            valor_pratos.append(valor_prato)
        case 5:
            prato = 'código 5 - Moqueca'
            pratos.append(prato)
            valor_prato = 32.0
            valor_pratos.append(valor_prato)
        case 6:
            prato = 'código 6 - Yakisoba'
            pratos.append(prato)
            valor_prato = 45.0
            valor_pratos.append(valor_prato)
        case 7:
            prato = 'código 7 - Espetinho'
            pratos.append(prato)
            valor_prato = 10.0
            valor_pratos.append(valor_prato)

    sleep(1.1)
    system('cls || clear')
    return


def menu():
    while True:
        print('----------------------------------')
        print('| código |  prato     | valor R$ |')
        print('|--------------------------------|')
        print('|   1    | Lasanha    |  40,00   |')
        print('|   2    | Feijoada   |  40,00   |')
        print('|   3    | Strogonoff |  37,00   |')
        print('|   4    | Mocotó     |  25,00   |')
        print('|   5    | Moqueca    |  32,00   |')
        print('|   6    | Yakisoba   |  45,00   |')
        print('|   7    | Espetinho  |  10,00   |')
        print('----------------------------------')
        cod = int(input(''))
        while cod < 1 or cod > 7:
            cod = int(input('Opção inválida! Digite o código\n'))

        valida_codigo(cod)

        print('----------------------------------')
        print('| código |        descrição      |')
        print('|--------------------------------|')
        print('|   1    | adicionar outro prato |')
        print('|   2    | ir para o pagamento   |')
        cod_2 = int(input('----------------------------------'))
        while cod_2 < 1 or cod_2 > 2:
            cod_2 = int(input('Opção inválida! Digite o código\n'))
        if cod_2 == 2:
            forma_pagamento()


menu()
