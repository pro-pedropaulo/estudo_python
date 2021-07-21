import random
n = random.randint(1,5)
meu_palpite = int(input('MEU PALPITE É: '))
tentativas = 1
while meu_palpite != n:
    print('VOCÊ ERROU TENTE NOVAMENTE: ')
    tentativas += 1
    n = random.randint(1, 5)
    meu_palpite = int(input('MEU PALPITE É: '))
print('VOCÊ ACERTOOOOU')
if tentativas == 1:
    print('EITA PARABÉNS VOCE ACERTOU DE PRIMEIRA')
elif tentativas <3:
    print('PARABÉNS VOCÊ FOI MUITO BEM')
elif tentativas <7:
    print('PARABÉNS VOCE CONSEGUIU EM UM NUMERO BOM DE TENTATIVAS')
else:
    print('PARABÉNS VOCE ACERTOU MAS NÃO FOI TÃO RÁPIDO')
print('precisou de {} tentativas'.format(tentativas))
