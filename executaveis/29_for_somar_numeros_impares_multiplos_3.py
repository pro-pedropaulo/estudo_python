soma = 0
acumula = 0
for c in range(1,500):
    if (c % 2) == 1 and (c % 3) == 0:
        soma += c
        acumula += 1
        print(c)
print('o total somado é {}'.format(soma))
print('O total de numeros são {}'.format(acumula))