"""
crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'
"""
cidade = input('Digite o nome de uma cidade: ').strip().title().split()

# resp = 'Santo' in cidade.split()[0]
# ou:
# print(f'O primeiro nome da cidade é "Santo"? ', 'Santo' in cidade.split()[0])
# ou:
print('O primeiro nome da cidade é "Santo"?', cidade[0].title() == 'Santo')
