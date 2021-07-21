import random
import time
pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'
jogadas = [pedra, papel, tesoura]
maquina_jogada = random.choice(jogadas)
print('PREPARE-SE PARA SUA JOGADA')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
escolha = int(input('FAÇA SUA JOGADA '))
time.sleep(2)
print('A Maquina escolheu {}'.format(maquina_jogada))
if maquina_jogada == pedra:
    if escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('VOCÊ GANHOU')
    elif escolha == 3:
        print('A MAQUINA GANHOU')
if maquina_jogada == papel:
     if escolha == 1:
         print('A MAQUINA GANHOU')
     if escolha == 2:
         print('EMPATE')
     if escolha == 3:
         print('VOCÊ GANHOU')
if maquina_jogada == tesoura:
    if escolha == 1:
        print('VOCE GANHOU')
    if escolha == 2:
        print('A MAQUINA GANHOU')
    if escolha == 3:
        print('EMPATOU')
elif escolha > 3:
    print('ESCOLHA UMA OPÇÃO VALIDA')
print('OBRIGADO POR JOGAR')