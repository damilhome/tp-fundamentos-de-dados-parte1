'''
Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.
'''

opcao_1 = 0
opcao_2 = 0
opcao_3 = 0

while True:
    print('''
[1] - Opção 1
[2] - Opção 2
[3] - Opção 3
[0] - Sair
''')
    try:
        voto = int(input('Escolha uma opção para votar: '))
    except:
        print('Valor não numérico digitado')
        continue

    match (voto):
        case 1:
            opcao_1 += 1
        case 2:
            opcao_2 += 1
        case 3:
            opcao_3 += 1
        case 0:
            break
        case _:
            print('Opção inválida')
            continue

print('Total:')
print(f'Opção 1: {opcao_1} votos')
print(f'Opção 2: {opcao_2} votos')
print(f'Opção 3: {opcao_3} votos')