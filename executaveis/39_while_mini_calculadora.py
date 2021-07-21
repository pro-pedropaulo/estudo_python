sair = False
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
maior = n1
while not sair:
    print('[ 1 ] SOMAR')
    print('[ 2 ] SUBTRAIR')
    print('[ 3 ] MAIOR NUMERO')
    print('[ 4 ] NOVOS NUMEROS')
    print('[ 5 ] SAIR PROGRAMA')
    escolha = int(input('DIGITE A AÇÃO: '))
    if escolha == 1:
        resultado_soma = n1 + n2
        print('----------------------------------------------------')
        print('A soma de {} + {} é {}'.format(n1,n2,resultado_soma))
        print('----------------------------------------------------')
    if escolha == 2:
        resultado_subtrair = n1 - n2
        print('----------------------------------------------------')
        print('A Subtração de {} - {} é {}'.format(n1,n2,resultado_subtrair))
        print('----------------------------------------------------')
    if escolha == 3:
        if n1 < n2:
            print('----------------------------------------------------')
            print('o Segundo numero o {} é maior'.format(n2))
            print('----------------------------------------------------')
        else:
            print('----------------------------------------------------')
            print('O maior numero é o {} o primeiro digitado'.format(maior))
            print('----------------------------------------------------')
    if escolha == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    if escolha == 5:
        sair = True
print('OBRIGADO POR USAR A CALCULADORA')