quantidade_pessoas = int(input('QUANTAS PESSOAS VÃO PARTICIPAR DA PESQUISA? '))
mediaidade = 0
soma_idade = 0
maioridade = 0
nome_mais_velho = ''
mulheres_novas = 0
for c in range (1, quantidade_pessoas + 1):
    nome = input('DIGITE O NOME DA PESSOA NUMERO {} '.format(c))
    sexo = input('DIGITE O SEXO DA PESSOA NUMERO {},  M / F '.format(c)).upper()
    idade = int(input('DIGITE A IDADE DA PESSOA NUMERO {} '.format(c)))
    soma_idade += idade
    mediaidade = soma_idade / quantidade_pessoas
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_novas += 1
print('A media da idade é {}'.format(mediaidade))
print('O nome do mais velho é {}, ele tem {} anos'.format(nome_mais_velho,maioridade))
print('O numero de mulheres que tem menos de 20 anos são {}'.format(mulheres_novas))