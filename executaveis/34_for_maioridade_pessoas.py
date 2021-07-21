ano_atual = 2021
quantidade_pessoas = int(input('QUANTAS PESSOAS VÃO SE INSCREVER '))
maior_idade = 0
menor_idade = 0
for c in range(0,quantidade_pessoas):
    nome = input('QUAL O NOME ? ')
    nascimento = int(input('QUAL O ANO DE NASCIMENTO ? '))
    verificar_idade = ano_atual - nascimento
    if verificar_idade >=18:
        maior_idade += 1
    if verificar_idade <18:
        menor_idade += 1
print('na lista há {} Maiores de idade e {} menores de idade'.format(maior_idade,menor_idade))