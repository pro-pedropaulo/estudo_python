numeros = [ [],[] ]
valor = 0
for c in range (1,10):
    valor = int(input('DIGITE UM NUMERO '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    if valor % 2 == 1:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'A lista dos numeros pares digitados é {numeros[0]}')
print(f'A Lista dos numeros Impares digitados é {numeros[1]}')