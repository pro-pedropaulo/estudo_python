km = int(input('Quantos KM dura a viagem '))
if km < 200:
    km_atualizado = km * 0.50
    print("O valor da viagem é R${:.2f} reais".format(km_atualizado))
else:
    km_atualizado_maior = km * 0.45
    print('O valor da viagem é R${:.2f} reais'.format(km_atualizado_maior))
print("BOA VIAGEM")