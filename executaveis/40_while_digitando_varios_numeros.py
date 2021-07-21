n1 = int(input('Digite um numero para de 0 a 998 para somar ou 999 para sair '))
soma = 0
somando_alto = 0
quantidade = 0
while n1 != 999:
        if n1 > 1000:
                print('DIGITE UM NUMERO VALIDO')
                print('A SOMA ATÉ AGORA DEU {}'.format(soma))
                n1 = int(input('Digite um numero para de 0 a 998 para somar ou 999 para sair '))
        else:
                soma += + n1
                quantidade += + 1
                print('--------------------------------------')
                print('A SOMA ATÉ AGORA DEU {}'.format(soma))
                print('--------------------------------------')
                n1 = int(input('Digite um numero para de 0 a 998 para somar ou 999 para sair '))
print('A soma total foi {}'.format(soma))
print('Foram digitados {} numeros'.format(quantidade))
