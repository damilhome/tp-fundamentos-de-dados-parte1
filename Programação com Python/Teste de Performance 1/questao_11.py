'''
Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
'''
import random

is_error = False
contador = 0

try:
    numero = int(input('Digite quantos dados deseja jogar: '))
except:
    is_error = True
    print('Valor não numérico digitado.')

if(not is_error):
    while(contador < numero):
        dado = random.randint(1, 6)
        print(f'Dado {contador + 1}: {dado}')
        contador += 1