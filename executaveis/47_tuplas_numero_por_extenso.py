contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez' )
numero = int(input('DIGITE UM NUMERO: '))
while True:
    if numero >0 and numero <11:
        print(f'O numero digitado foi {contagem[numero]}')
        quer_continuar = input('QUER CONTINUAR S/N ').upper()
        if quer_continuar == 'S':
            numero = int(input('DIGITE UM NUMERO: '))
        if quer_continuar == 'N':
            break
    else:
        print('DIGITE UM NUMERO DE 0 A 10')
        numero = int(input('DIGITE UM NUMERO: '))

print('FIM DO PROGRAMA')
