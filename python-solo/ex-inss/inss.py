from os import system
from time import sleep


def resultados(nome_cad, senha_cad, salario_funcionario, desconto_inss, desconto_irrf, desconto_transporte,
               desconto_saude, desconto_refeicao, salario_liquido):
    nome = input('Nome: ').strip().title()
    senha = input('Senha: ').strip()

    while nome != nome_cad or senha != senha_cad:
        print('Nome e/ou senha incorreto(s)!')
        sleep(1.1)
        system('cls || clear')
        nome = input('Nome: ').strip().title()
        senha = input('Senha: ').strip()

    sleep(1)
    system('cls || clear')

    print('----------------------------------')
    print('Folha de Pagamento')
    print('==================================')
    print(f'Nome do funcionário: {nome}')
    print(f'Salário bruto: R$ {salario_funcionario:.2f}')
    print('----------------------------------------')
    print('Descontos')
    print('----------------------------------------')
    print(f'INSS: R$: {desconto_inss:.2f}')
    print(f'IRRF: R$ {desconto_irrf:.2f}')
    print(f'Vale-transporte: R$ {desconto_transporte:.2f}')
    print(f'Plano de saúde: R$ {desconto_saude:.2f}')
    print(f'Vale-refeição: R$ {desconto_refeicao:.2f}')
    print('----------------------------------------')
    print(f'Salário líquido: R$ {salario_liquido:.2f}')
    print('----------------------------------------')


def calcula_refeicao(salario):
    vale_dia = float(input('Valor do vale-refeição por dia: '))
    valor_dias = vale_dia * 22
    desconto_min = 0.12
    desconto_max = 0.2

    valor_refeicao = 0
    if valor_dias <= (salario - salario * desconto_max):
        valor_refeicao = valor_dias - (valor_dias * desconto_min)
        return valor_refeicao
    else:
        valor_refeicao = valor_dias - (valor_dias * desconto_max)
        return valor_refeicao


def calcula_transporte(salario, resp_trans):
    valor_vt = 0
    if resp_trans == 's':
        valor_vt = (salario * 0.06)
        return valor_vt
    else:
        return valor_vt


def calcula_irrf(valor_base, qtd_dependentes):
    valor_dependente = 189.59
    desconto_dependentes = qtd_dependentes * valor_dependente
    valor_base -= desconto_dependentes

    if valor_base <= 2259.20:
        irrf = 0
        deduzir = 0
    if valor_base <= 2826.65:
        irrf = 0.075
        deduzir = 169.44
    elif valor_base <= 3751.05:
        irrf = 0.15
        deduzir = 381.44
    elif valor_base <= 4664.68:
        irrf = 0.225
        deduzir = 662.77
    else:
        irrf = 0.275
        deduzir = 896.0

    valor_base = (valor_base * irrf) - deduzir
    irrf_desconto = valor_base

    return irrf_desconto


def calcula_inss(salario):
    imposto = 0
    if salario <= 1412.0:
        imposto = 0.075
    elif salario <= 2666.68:
        imposto = 0.09
    elif salario <= 4000.03:
        imposto = 0.12
    elif salario <= 7786.02:
        imposto = 0.14

    desconto_inss = salario * imposto
    base_irrf = salario - desconto_inss

    return desconto_inss, base_irrf


def perguntas():
    salario = float(input('Digite o seu salário: R$ '))
    resp_transporte = input('Você deseja receber vale-transporte? (s / n) ').strip().lower()
    resp_dependentes = int(input('Quantos dependentes você possui? '))
    while resp_dependentes < 0 or resp_dependentes > 2:
        print('Quantidade máxima: 2')
        resp_dependentes = int(input('Quantos dependentes você possui? '))

    return salario, resp_transporte, resp_dependentes


def comeco():
    print('---------------------------')
    nome_cadastro = input('Digite o seu nome: ').strip().title()
    senha_cadastro = input('Digite uma senha: ').strip()

    salario, transporte, dependentes = perguntas()
    valor_inss, base_irrf = calcula_inss(salario)
    valor_irrf = calcula_irrf(base_irrf, dependentes)
    vale_saude = 150.0
    valor_transporte = calcula_transporte(salario, transporte)
    vale_refeicao = calcula_refeicao(salario)

    salario_f = salario
    salario_f -= valor_inss
    salario_f -= valor_irrf
    salario_f -= valor_transporte
    salario_f -= vale_saude
    salario_f -= vale_refeicao

    resultados(nome_cadastro, senha_cadastro, salario, valor_inss, valor_irrf, valor_transporte, vale_saude,
               vale_refeicao, salario_f)


comeco()
