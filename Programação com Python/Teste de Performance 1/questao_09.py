'''
Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%.
'''

is_error = False

try:
    valor = input('Digite o valor da compra: ')
    valor = valor.replace(',', '.')
    valor = float(valor)
except:
    is_error = True
    print('Valor não numérico digitado.')

if(not is_error):
    if(valor > 500):
        valor = valor * 0.75
        print(f'Valor com desconto de 25%: R${valor:.2f}')
    elif(valor > 350):
        valor = valor * 0.80
        print(f'Valor com desconto de 20%: R${valor:.2f}')
    elif(valor > 200):
        valor = valor * 0.85
        print(f'Valor com desconto de 15%: R${valor:.2f}')
    elif(valor > 100):
        valor = valor * 0.90
        print(f'Valor com desconto de 10%: R${valor:.2f}')
    else:
        print(f'Valor sem desconto: R${valor:.2f}')
