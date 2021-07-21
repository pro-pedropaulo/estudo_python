import random
n = random.randint(0,5)
escolha = int(input('Escolha um numero de 0 a 5: '))
if escolha == n:
    print('PARABÉNS VOCE GANHOU O JOGO')
else:
    print('Tente outra vez')
print('O numero sorteado foi {}'.format(n))