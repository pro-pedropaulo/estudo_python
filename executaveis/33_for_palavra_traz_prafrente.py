frase = input('DIGITE UMA FRASE: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
print('VOCE DIGITOU A FRASE {}'.format(junto))
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palidromo! ')
else:
    print('A FRASE DIGITADA NÃO É UM PALIDROMO')