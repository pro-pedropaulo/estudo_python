listagem = ('Borracha', 2.00,
            'Caderno', 7.55,
            'Caneta', 1.99,
            'Lapiz', 1.10,
            'Corretivo', 2.15,)

print('-' *30)
print(f'{"LISTAGEM DE PREÇO":^30}')
print('-' *30)

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R$ {listagem[c]:.>10.2f}')