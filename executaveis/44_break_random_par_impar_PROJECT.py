import random
maquina = 0
vitoria = 0
resultado = ''
contagem_vitoria = 0
while True:
    print('-' * 40)
    sua_aposta = int(input('DIGITE UM NUMERO DE 0 A 10 '))
    while sua_aposta >10 or sua_aposta <0:
        sua_aposta = int(input('DIGITE UM NUMERO DE 0 A 10 '))
    maquina = random.randint(1, 10)
    par_impar = input('[P / I] ').strip() [0]
    conta = maquina + sua_aposta
    if (conta % 2) == 0:
        resultado = 'p'
    elif (conta % 2) == 1:
        resultado = 'i'
    if resultado == par_impar:
        print('VOCE GANHOU')
        contagem_vitoria += 1
    else:
        print('VOCÊ PERDEU')
        break
    print(f'A MAQUINA JOGOU {maquina}')
if contagem_vitoria <1:
        print('VOCÊ NÃO GANHOU NENHUMA VEZ')
else:
    print(f'Voce ganhou {contagem_vitoria} partidas seguidas antes de perder')