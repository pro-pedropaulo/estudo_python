valores = []
continuar = ''
while True:
    n = int(input('DIGITE UM VALOR '))
    if n not in valores:
        valores.append(n)
        print('VALOR ADICIONADO COM SUCESSO')
    else:
        print('VALOR JÁ CADASTRADO')
    continuar = input('DESEJA CONTINUAR [S] [N] ').upper()
    if continuar == 'N':
        break
valores.sort()
print(f'VOCE DIGITOU OS VALORES {valores}')
