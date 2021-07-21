n1 = 0
continuar = 'S'
soma = 0
contagem = 0
maior = 0
menor = 0
while continuar not in 'Nn':
    n1 = int(input('DIGITE UM NUMERO: '))
    soma += n1
    contagem += 1
    continuar = input('QUER CONTINUAR?   [S/N] ')
    menor = n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
media = soma / contagem
print('FORAM DIGITADOS {} NUMEROS'.format(contagem))
print('A MÉDIA DOS NUMEROS DIGITADOS É {:.1f}'.format(media))
print('O MAIOR NUMERO DIGITADO FOI {}'.format(maior))
print('O MENOR NUMERO DIGITADO FOI {}'.format(menor))