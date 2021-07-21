numero = int(input('QUAL NUMERO QUER SABER A TABUADA? '))
total = int(input('QUANTAS VEZES QUER REPETIR A TABUADA? '))
contagem = 0
for c in range(contagem, total + 1):
    resultado = numero * contagem
    print("O numero {} X {} dá {}".format(numero,contagem,resultado))
    contagem += 1
print('OBRIGADO POR USAR A CALCULADORA')