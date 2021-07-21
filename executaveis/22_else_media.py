n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
n3 = float(input('Digite a terceira nota '))
n4 = float(input('Digite a quarta nota '))
media = (n1 + n2 + n3 + n4) / 4
print('A sua média foi {}'.format(media))
if media > 7 and media <= 9:
    print('Parabéns  voce foi aprovado')
elif media > 9.1:
    print('Parabens voce tirou umas das melhores notas da escola')
elif media >= 5 and media <= 6.9:
    print('Voce está de recuperação')
elif media <5:
    print('Você está Reprovado')
else:
    print('Confirme os dados digitados')
