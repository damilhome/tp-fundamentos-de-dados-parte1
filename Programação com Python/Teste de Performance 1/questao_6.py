'''
Escreva um programa onde o usuário deve adivinhar um número secreto. 
O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
'''
import random

numero_secreto = random.randint(1, 10)

escolha_do_usuario = 0

while (not escolha_do_usuario == numero_secreto):
    try:
        escolha_do_usuario = int(input('Tente adivinhar o número secreto (entre 1 e 10): '))

        if (escolha_do_usuario > numero_secreto):
            print('Muito alto')
        elif (escolha_do_usuario < numero_secreto):
            print('Muito baixo')
        else:
            print('Correto!')
    except:
        print('Valor não numérico digitado.')