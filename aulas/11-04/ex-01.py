#import os
#os.system('cls || clear')

fator: int

fator = int(input('Digite o valor a ser multiplicado: '))
for i in range(1,11):
     print(f'{fator} x {i} = {fator*i}')