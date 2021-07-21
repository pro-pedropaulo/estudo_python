contagem = 0
lista_peso = []
for c in range(1,7 + 1):
    peso = float(input('DIGITE O PESO DA PESSOA NUMERO {} '.format(c)))
    lista_peso.append(peso)
print('O maior peso é o', max(lista_peso))
print('O menor peso é o', min(lista_peso))
