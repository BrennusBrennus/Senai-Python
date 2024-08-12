from os import system


# função sem retorno
def logo_senai():
    system('cls || clear')
    print('=== SENAI ===')


# listas vazias para o armazenamento de dados do usuário
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []
imcs = []
mensagem = []


# função que retorna o IMC
def calcula_imc(altura_pessoa, peso_pessoa):
    return peso_pessoa / altura_pessoa.__pow__(2)


def mensagem_imc(imc_pessoa):
    aviso: str
    if imc_pessoa < 18.5:
        aviso = 'Abaixo do peso ideal'
    elif imc_pessoa < 25:
        aviso = 'Peso ideal'
    elif imc_pessoa < 30:
        aviso = 'Sobrepeso'
    elif imc_pessoa < 35:
        aviso = 'Obesidade grau I'
    elif imc_pessoa < 40:
        aviso = 'Obesidade grau II'
    else:
        aviso = 'Obesidade grau III'

    return aviso


# solicitando dados do usuário
def entrada_de_dados():
    while True:
        logo_senai()
        nome = input('Digite o seu nome. Para encerrar o programa, digite \"sair\": ').strip().lower()
        if nome == 'sair':
            imprime_dados()
            break
        else:
            sobrenome = input('Digite o seu sobrenome: ').strip().title()
            nome = nome.title()

        idade = int(input('Idade: '))
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))

        imc = calcula_imc(altura, peso)
        resultado_imc = mensagem_imc(imc)

        # adicionando os dados inseridos às listas
        nomes.append(nome)
        sobrenomes.append(sobrenome)
        idades.append(idade)
        pesos.append(peso)
        alturas.append(altura)
        imcs.append(imc)
        mensagem.append(resultado_imc)


# exibindo os dados armazenados
def imprime_dados():
    logo_senai()
    for i in range(len(nomes)):
        print(f'Usuário {i + 1}')
        print('Nome:', nomes[i], sobrenomes[i])
        print('Idade:', idades[i], ' anos')
        print('Peso:', pesos[i], 'Kg')
        print('Altura:', alturas[i], 'metros')
        print(f'IMC: {imcs[i]:.2f}. {mensagem[i]}')


# começo do programa
entrada_de_dados()
