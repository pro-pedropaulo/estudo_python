import datetime
ano = int(input('Digite o ano que queira verificar : '))
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é Bisexto'.format(ano))
else:
    print('O ano {} não é Bisexto'.format(ano))