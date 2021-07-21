produto = input('Digite o nome do produto que queira comprar: ')
valor = float(input('Qual é o valor do produto {} escolhido '.format(produto)))
print('MÉTODOS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] à vista no cartão: 5% de desconto')
print('[ 3 ] em até 2x no cartão: preço formal ')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
print('[ 5 ] Não irei realizar a compra')
escolha = int(input('ESCOLHA A OPÇÃO QUE DESEJA: '))
if escolha == 1:
    novo_valor = valor - valor / 100 * 10
    print('O valor atualizado do(a) {} é R${:.2f} reais'.format(produto,novo_valor))
elif escolha == 2:
    novo_valor = valor - valor / 100 * 5
    print('O valor atualizado do(a) {} é R${:.2f} reais'.format(produto,novo_valor))
elif escolha == 3:
    novo_valor = valor / 2
    print('O produto {} terá o seu preço normal, parcelado em 2 vezes de {:.2f}'.format(produto,novo_valor))
elif escolha ==4:
    quantidade_parcela = int(input('em quantas vezes quer parcelar ? '))
    novo_valor = valor + valor / 100 * 20
    novo_valor_parcelado = novo_valor / quantidade_parcela
    print('O produto {} parcelado em {} vezes terá o seu preço atualizado de {:.2f} e suas parcelas serão de {:.2f}'
          .format(produto,quantidade_parcela,novo_valor,novo_valor_parcelado))
elif escolha == 5:
    pergunta_cliente = input('CERTEZA QUE NÃO QUER O PRODUTO ?  SIM / NÃO ').lower()
    if pergunta_cliente == 'sim':
        print('OK caso queira escolher outro estamos a disposição')
    if pergunta_cliente == 'não' or 'nao':
        print('reinicie o programa para começar a escolha do produto')
elif escolha > 5:
    print('POR FAVOR DIGITE AS OPÇÕES CORRETAS PARA PROSEGUIMOS COM A COMPRA')
print('AS LOJAS PP AGRADECE A SUA PREFERENCIA ')
