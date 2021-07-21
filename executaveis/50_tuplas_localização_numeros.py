numero = (int(input('Digite o primeiro numero '))) , (int(input('Digite o segundo numero '))), (int(input('Digite o terceiro numero '))) , (int(input('Digite o quarto numero numero ')))
par = 0
print(numero)
valor_saber = int(input('QUAL VALOR QUER REALIZAR A ANALISE ? '))
if valor_saber not in numero:
    print('O NUMERO QUE QUER ANALISAR NÃO FOI DIGITADO')
else:
    print(f'O valor {valor_saber} apareceu {numero.count(valor_saber)} vezes')
    print(f'O valor {valor_saber} apareceu pela primeira vez na posição {numero.index(valor_saber)+1}')
for c in numero:
    if c % 2 == 0:
        par += 1
        print(f'os valores pares digitados foram {par}')