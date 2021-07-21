n = 0
soma = 0
contagem = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999 or n == 0:
        break
    soma += n
    contagem += 1
print(f'O total de numeros digitados foram {contagem} e a soma foi {soma}')