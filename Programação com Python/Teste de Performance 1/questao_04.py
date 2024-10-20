'''
Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão)
e dois números, e então execute a operação escolhida com os números.
'''

print(''' 
[1] - Adição
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
      
''')
is_error = False

try:
    operacao = int(input('Escolha uma operação: '))
    num_1 = int(input('Primeiro número: '))
    num_2 = int(input('Segundo número: '))
except:
    is_error = True
    print('Valor não numérico digitado.')

if(not is_error):
    match operacao:
        case 1:
           print(f'{num_1} + {num_2} = {num_1 + num_2}')
        case 2:
           print(f'{num_1} - {num_2} = {num_1 - num_2}')
        case 3:
            print(f'{num_1} * {num_2} = {num_1 * num_2}')
        case 4:
            if(not num_2 == 0):
                print(f'{num_1} / {num_2} = {num_1 / num_2}')
            else:
                print('Operação inválida, divisão por zero.')
        case _:
            print('Operação inválida.')
