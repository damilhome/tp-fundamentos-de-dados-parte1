'''
Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
'''

'''
IMC= peso (kg) / altura (m)2

O resultado do IMC é interpretado da seguinte forma1:

Menor que 18,5: Magreza
18,5 a 24,9: Peso normal
25 a 29,9: Sobrepeso
30 a 34,9: Obesidade grau I
35 a 39,9: Obesidade grau II
Maior que 40: Obesidade grau III
'''

is_error = False

try:
    peso = input('Digite seu pego (em kg): ')
    # O usuário pode acabar digitando o número com vírgula ao invés de ponto
    peso = peso.replace(',', '.')
    peso = float(peso)

    altura = input('Digite sua altura (em metro): ')
    # O usuário pode acabar digitando o número com vírgula ao invés de ponto
    altura = altura.replace(',', '.')
    altura = float(altura)
except:
    is_error = True
    print('Valor não numerico digitado')

if(not is_error):
    imc = peso / (altura ** 2)

    if(imc < 18.5):
        print('Muito magro')
    elif(imc < 25):
        print('Peso normal')
    elif(imc < 30):
        print('Sobrepeso')
    elif(imc < 35):
        print('Obesidade grau I')
    elif(imc < 40):
        print('Obesidade grau II')
    else:
        print('Obesidade grau III')