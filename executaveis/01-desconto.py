nome = input('Digite o nome da pessoa: ')
salario = float(input('Digite o Salario da pessoa: '))
desconto = float(input('Digite a porcertagem de desconto do salario: '))
salario_final = salario - (salario / desconto)

print('{}, tem o Salário de R${:.2f}, mas houve desconto de {}%, o salario final do mes foi R${:.2f}'.format(nome,salario,desconto,salario_final))