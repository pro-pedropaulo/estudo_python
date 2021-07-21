valores = []
valores_par = []
valores_impar = []
continuar = ''
contagem_numeros = 0
while True:
    n = int(input('DIGITE UM NUMERO: '))
    if (n % 2) == 0:
        valores.append(n)
        valores_par.append(n)
    if (n % 2) == 1:
        valores.append(n)
        valores_impar.append(n)
    print('VALOR ADICIONADO')
    contagem_numeros += 1
    continuar = input('QUER CONTINUAR ? [S] [N] ').upper()
    while continuar not in 'NnSs':
        print('Digite S para continuar ou N para sair')
        continuar = input('QUER CONTINUAR ? [S] [N] ').upper()
    if continuar == 'N':
        break
print(f'foram adicionandos {contagem_numeros} numeros')
print(f'A lista completa é {valores}')
print(f'A lista com os numeros pares são {valores_par}')
print(f'A lista com os numeros impares são {valores_impar}')
