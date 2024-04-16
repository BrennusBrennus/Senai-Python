"""
para importar uma biblioteca:

    import algo (importa todo o conteudo de uma bliblioteca)
    import num (1, 2, 3, 4, 5, ...)

    para importar somente o necessario:
    from algo import alguma_coisa
    from num import 5
"""
import math
from math import sqrt
from math import trunc

num = int(input('Digite um número: '))
print('\nCom as funções sqrt() e trunc()')
print(f'Raíz quadrada de {num}:', trunc(sqrt(num)))

print('\nSem sem as funções sqrt() e trunc()')
print(f'Raíz quadrada de {num}: {num**0.5:.0f}')
