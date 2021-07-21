soma_par = 0
soma_impar = 0
acumula_par = 0
acumula_impar = 0
for c in range(0, 6):
    n = int(input('Digite um numero inteiro: '))
    if (n % 2) == 0:
        soma_par += n
        acumula_par += 1
    if (n % 2) == 1:
        soma_impar += n
        acumula_impar += 1
print('Foram digitados {} numeros pares e a soma deu o resultado de {}'.format(acumula_par,soma_par))
print('Foram digitados {} numeros impares e a soma deu o resultado de {}'.format(acumula_impar,soma_impar))
print('FIM')