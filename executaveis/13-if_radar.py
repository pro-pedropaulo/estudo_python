velocidade = int(input('sua velocidade: '))
taxa_multa = 7
superior = (velocidade - 80) * taxa_multa
if velocidade > 80:
    print("VOCE ESTÁ MULTADO")
    print("A Taxa da cidade é {} por KM ultrapassado".format(taxa_multa))
    print('O valor da multa é R$ {} reais'.format(superior))
else:
    print("PARABÉNS CONTINUE DIRIGINDO COM PRUDENCIA")
print('BOA VIAGEM')
