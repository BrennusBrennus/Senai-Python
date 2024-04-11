import os 

os.system('cls || clear')

username_registered = 'Breno'
password_registered = '123'

username_login = input('Usuário: ')
password_login = input('Senha: ')

if password_login == password_registered and username_login == username_registered:
    print(f'Bem-vindo, {username_registered}')
else:
    print('Acesso negado!')
