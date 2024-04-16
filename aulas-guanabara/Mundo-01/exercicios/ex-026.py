"""
crie um progrma que leia uma frase pelo teclado e mostre:
> quantas vezes aparece a letra "A";
> em que posição ela aparece pela primeira vez;
> em que posição ela aparece pela última vez.
"""

frase = input('Digite uma frase qualquer: ').lower().strip()

print(f'Quantidade de vezes em que a letra A aparece: {frase.count('a')}')
print(f'Posição (índice) em que ela aparece pela primeira vez: {frase.find('a')}')
print(f'Posição (índice) em que ela aparece pela última vez: {frase.find('a', -1)}')
