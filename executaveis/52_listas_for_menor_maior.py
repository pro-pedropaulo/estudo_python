valores = []
maior_valor = 0
menor_numero = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicãp {c} ')))
    if c == 0:
        maior_valor = valores[c]
        menor_numero = valores[c]
    else:
        if valores[c] > maior_valor:
            maior_valor = valores[c]
        if valores[c] < menor_numero:
            menor_numero = valores[c]
print(valores)
print(f'O maior valor digitado foi o {max(valores)}')
for posicao, valor in enumerate(valores):
    if valor == maior_valor:
        print(f'QUE ESTÁ NA POSIÇÃO {posicao}')
print(f'O menor numero digitado foi o {min(valores)}')
for posicao, valor in enumerate(valores):
    if valor == menor_numero:
        print(f'QUE ESTÁ NA POSIÇÃO {posicao}')
print('FIM')