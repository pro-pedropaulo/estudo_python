valor_casa = float(input('QUAL O VALOR TOTAL DA CASA? '))
salario = float(input('QUAL O SEU SALARIO EM REAIS? '))
parcelas = int(input('QUANTOS ANOS QUER PAGAR A CASA ?? '))
parcelas = parcelas * 12
valor_parcela = valor_casa / parcelas
if salario > (valor_parcela * 100) / 30:
    print('Emprestimo aprovado')
else:
    print('Infelizmente o emprestimo foi negado')
print('Você tem que pagar em {} meses o valor de R$ {:.2f} reais'.format(parcelas,valor_parcela))
