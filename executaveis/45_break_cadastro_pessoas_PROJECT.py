idade = 0
sexo = ''
masculino = feminino = maior_idade = menor_idade = mulher_menos_vinte = outros = 0
while True:
    print('-' * 30)
    print('CADASTRO DE PESSOAS')
    print('-' * 30)
    idade = int(input('QUAL A IDADE? '))
    while idade > 105 or idade < 0:
        print('DIGITE UMA IDADE VALIDA')
        idade = int(input('QUAL A IDADE? '))
    if idade > 18:
        maior_idade += 1
    else:
        menor_idade += 1
    sexo = input('QUAL O SEXO [M / F / O]? ').strip().upper()[0]
    while sexo not in 'mMfFOo':
        print('DIGITE M para masculino ou F para feminino ou O para Outros')
        sexo = input('QUAL O SEXO [M / F / O]? ').strip().upper()[0]
    if sexo in 'Oo':
        outros += 1
    if sexo in 'Mm':
        masculino += 1
    if sexo in 'Ff':
        feminino += 1
    if sexo in 'Ff' and idade < 20:
        mulher_menos_vinte += 1
    print('-' * 30)
    continua = input('QUER CONTINUAR [S / N]').strip().upper()[0]
    while continua not in 'SsNn':
        print('POR FAVOR DIGITE S para continuar ou S para sair')
        continua = input('QUER CONTINUAR [S / N]').strip().upper()[0]
    if continua in 'Nn':
        break
print(f'FORAM ADICIONADOS {masculino} HOMENS')
print(f'FORAM ADICIONADAS {feminino} MULHERES')
print(f'FORAM ADICIONADOS {outros} PESSOAS COM OUTRAS SEXUALIDADES')
print(f'FORAM ADICIONADOS {maior_idade} MAIORES DE IDADE')
print(f'FORAM ADICIONADOS {menor_idade} MENORES DE IDADE')
print(f'FORAM ADICIONADAS {mulher_menos_vinte} MULHER COM MENOS DE 20 ANOS')