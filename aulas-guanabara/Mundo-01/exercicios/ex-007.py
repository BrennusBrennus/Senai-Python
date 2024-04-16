# crie um programa que leia duas notas de um aluno e mostre a média

nota_um = float(input('primeira nota: '))
nota_dois = float(input('segunda nota: '))

media = (nota_um + nota_dois) / 2
print(f'Média aritmética: {media:.1f}')

mediaPonderada = (nota_um * 3 + nota_dois * 7) / (3 + 7)
print(f'Média ponderada: {mediaPonderada:.1f}')
