principal = []
temp = []
pessoas = 0
mais_velho = 0
mais_novo = 0
maior_idade = 0
while True:
    temp.append(str(input('Digite o nome ')))
    pessoas += 1
    temp.append(int(input('Digite a Idade ')))
    if temp [1] > 21:
        maior_idade += 1
    if len(principal) == 0:
        mais_velho = temp[1]
        mais_novo = temp[1]
    else:
        if temp[1] > mais_velho:
            mais_velho = temp[1]
        if temp[1] < mais_novo:
            mais_novo = temp[1]
    principal.append((temp[:]))
    temp.clear()
    continuar = input('QUER CONTINUAR ? [S] [N] ').upper()
    if continuar == 'N':
        break
print(principal)
print(f'Foram cadastradas {pessoas} pessoas')
for p in principal:
    if p[1] == mais_velho:
        print(f"O mais velho da lista é o {p[0]} com {p[1]} anos ")
for p in principal:
    if p[1] == mais_novo:
        print(f'O mais novo da lista é o {p[0]} com {p[1]} anos')
print(f'Na lista há {maior_idade} maiores de idade')