ano_atual = 2021
nome_nadador = input('Qual o nome do nadador? ')
idade_nadador = int(input('Qual ano {} nasceu? '.format(nome_nadador)))
idade_atual = ano_atual - idade_nadador
print('{} tem {} anos'.format(nome_nadador,idade_atual))
if idade_atual <9:
    print('o futuro nadador {} é da categoria mirim'.format(nome_nadador))
elif idade_atual >= 9 and idade_atual < 14:
    print('O futuro nadador {} é da categoria infantil'.format(nome_nadador))
elif idade_atual >= 14 and idade_atual <19:
    print('O futuro nadador {} é da categoria junior'.format(nome_nadador))
elif idade_atual >= 19 and idade_atual <25:
    print('O futuro nadador {} é da categoria Senior'.format(nome_nadador))
elif idade_atual >= 25 and idade_atual <85:
    print('O futuro nadador {} é da categoria master'.format(nome_nadador))
elif idade_atual > 85 and idade_atual <103:
    print('Infelizmente não aceitamos idosos dessa idade')
else:
    print('Informações incorretas')