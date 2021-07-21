soma = caro = valor_produto = quantidade_item = 0
valor_barato = valor_mais_caro = 0
nome_mais_barato = ''
nome_mais_caro = ''
while True:
    nome_produto = input('DIGITE O NOME DO PRODUTO: ')
    valor_produto = float(input('DIGITE O VALOR DO PRODUTO EM R$: '))
    soma += valor_produto
    quantidade_item += 1
    if quantidade_item == 1:
        valor_barato = valor_produto
        nome_mais_barato = nome_produto
        valor_mais_caro = valor_produto
        nome_mais_caro = nome_produto

    if valor_produto < valor_barato:
        valor_barato = valor_produto
        nome_mais_barato = nome_produto

    if valor_produto > valor_mais_caro:
        nome_mais_caro = nome_produto

    if valor_produto > 1000:
        caro += 1
    print('-' * 30)
    print('PRODUTO CADASTRADO')
    print('-' * 30)
    continuar = input('QUER CONTINUAR S/N ? ').upper()
    print('-' * 30)
    while continuar not in 'SsNn':
        print('POR FAVOR DIGITE S PARA CONTINUAR OU N PARA SAIR')
        continuar = input('QUER CONTINUAR S/N ? ').upper()
        print('-' * 30)
    if continuar in 'Nn':
        break
print(f'O total de gasto foi R$ {soma} reais')
if caro == 0:
    print('nenhum produto custa mais que R$1.000')
if caro == 1:
    print('Só um produto custa mais que R$1.000')
else:
    print(f'O total de {caro} Itens custa mais do que R$1.000')
print(f'Foram comprados o numero de {quantidade_item} itens')
print(f'O produto mais barato é o {nome_mais_barato} e custa {valor_barato:.2f}')
print(f'O produto mais caro é o {nome_mais_caro} e custa {valor_mais_caro:.2f}')