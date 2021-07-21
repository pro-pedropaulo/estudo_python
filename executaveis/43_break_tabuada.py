numero = 0
contagem = 0
total = 10
while True:
    numero = int(input('DIGITE O NUMERO QUE SERÁ MULTIPLICADO '))
    contagem = 0
    if numero < 0:
        break
    print('-' *30)
    for c in range(contagem, total + 1):
        resultado = numero * contagem
        print(f'O numero {numero} X {contagem} dá {resultado}')
        contagem += 1
    print('-' * 30)
print('OBRIGADO POR USAR A TABUADA ONLINE')