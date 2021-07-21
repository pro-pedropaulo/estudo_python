###iniciei as variaveis###

quantidade_soma = int(input('DIGITE QUANTAS PROGRESSOES DE SOMAS SERÃO FEITAS: '))
contagem = 0
resultado = 0
numero_somado = 0
resultado_antigo = 0
for c in range(contagem,quantidade_soma):   ##contagem
    if numero_somado == 0:                                            ##se numero somado começar com 0 immprimir frase
        print('VAMOS INICIAR DIGITE O PRIMEIRO NUMERO: ')
    numero_somado = int(input('DIGITE O NUMERO A SER SOMADO: '))     #instrução de entrada para numero somado
    resultado_antigo = resultado                #criei variavel resultado antigo com o ultimo regulstado
    resultado += numero_somado      # resultado recebe resultado anitgo + novo numero somado
    contagem += 1             #adiciona um numero na contagem
    print('ESSE É O {} NUMERO DIGITADO, A SOMA DE {} com {} = {}  '.format(contagem,resultado_antigo, numero_somado, resultado))
print('FIM')