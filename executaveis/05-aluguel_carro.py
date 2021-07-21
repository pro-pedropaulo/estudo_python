#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

carro = input('Qual carro voce alugou: ')
print('O custo é R$60 por dia e R$0,15 por Km rodado. ')
dias = int(input('Quantos dias voce ficou com o carro: '))
km = float(input("Quantos KM voce rodou: "))
valorfinal = (dias * 60) + (km * 0.15)
print('Para o {}, sendo que voce ficou {} dias, e rodou {:.2f} KM, o valor final é {:.2f}'.format(carro,dias,km,valorfinal))