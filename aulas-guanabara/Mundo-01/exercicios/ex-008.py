# crie um programa que leia um valor em metros e retorne ele em centímetros e milímetros

print('=== Conversor de metros para centímetros e milímetros ===')
metros = float(input('Digite um valor: '))

centimetros = metros * 10**2
milimetros = metros * 10**3

print(f'Centímetros: {centimetros:.2f}')
print(f'Milímetros: {milimetros:.2f}')
