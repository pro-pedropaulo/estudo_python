sexo = input('Digite o sexo da pessoa M/F ').upper().strip() [0]
soma_masculino = 0
soma_feminino = 0
while sexo not in 'MmFf':
    print('Digite por favor M ou F')
    sexo = input('Digite o sexo da pessoa M/F ou S para sair ').upper().strip()[0]
while sexo in 'mMfF':
    print('Sexo registrado')
    sexo = input('Digite o sexo da pessoa M/F ou S para sair ').upper().strip()[0]
    if sexo in 'Mm':
        soma_masculino += 1
    if sexo in 'Ff':
        soma_feminino += 1
while sexo in 'S':
    break
print('FIM DO PROGRAMA')
print('Foram digitados {} masculinos e foram digitados {} femininos'.format(soma_masculino,soma_feminino))