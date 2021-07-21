nome = input('Digite o seu nome: ')
altura = float(input('Digite sua altura '))
peso = float(input('Digite seu peso '))
imc = peso / (altura * altura)
if imc <18.5:
    print("{} está Abaixo do peso".format(nome))
elif imc <25:
    print('{} está Peso Ideal'.format(nome))
elif imc <30:
    print('{} está com Sobrepeso'.format(nome))
elif imc <40:
    print('{} está Obeso'.format(nome))
else:
    print('{} Está com obesidade morbida'.format(nome))
print('Obrigado por se consultar com a calculadora IMC')
