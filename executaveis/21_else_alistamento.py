ano_atual = 2021
ano_nascimento = int(input('Digite o ano de nascimento '))
calcular_ano = ano_atual - ano_nascimento
if calcular_ano > 18:
    print('você tem {} anos'.format(calcular_ano))
    atrasado = calcular_ano - 18
    print('Você está {} anos atrasados'.format(atrasado))
elif calcular_ano>17 and calcular_ano == 18:
    print('voce tem {} anos'.format(calcular_ano))
    print('Voce está na fase de alistamento')
else:
    print('voce tem {} anos'.format(calcular_ano))
    antecipado = 18 - calcular_ano
    print('Ainda não é sua hora, faltam {} anos '.format(antecipado))
print('Obrigado pela consulta brasil a frente.')