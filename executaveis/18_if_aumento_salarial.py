nome = input('Qual o nome do funcionario? ')
salario = float(input('Qual o salario do funcionario? '))
if salario > 1250:
    salario_reajuste = salario + (salario * 10 / 100)
    print('O novo salario do {} é de R${:.2f} reais'.format(nome,salario_reajuste))
if salario <= 1250:
    salario_reajuste = salario + (salario * 15 / 100)
    print('O novo salario do {} é de R${:.2f} reais'.format(nome,salario_reajuste))
print('PARABÉNS {} continue o otimo trabalho'.format(nome))
