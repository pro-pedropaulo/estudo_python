valores = []
continuar = ''
numeros_digitados = 0
verificador_cinco = 0
while True:
    n = int(input('DIGITE UM NUMERO: '))
    if n == 5:
        verificador_cinco += 1
    valores.append(n)
    numeros_digitados += 1
    print('VALOR ADICIONADO')
    continuar = input('QUER CONTINUAR [S] [N] ').upper()
    if continuar == 'N':
        break
print(valores)
print(f'FORAM DIGITADOS {numeros_digitados} NUMEROS')
valores.sort(reverse=True)
print(f"OS VALORES DIGITADOS EM ORDEM DECRECENTE FORAM {valores}")
if verificador_cinco >1:
    print(f'SIM HÁ O NUMERO 5 NA LISTA E FOI DIGITADO {verificador_cinco} VEZES')
if verificador_cinco == 0:
    print('NÃO FOI DIGITADO O NUMERO 5')