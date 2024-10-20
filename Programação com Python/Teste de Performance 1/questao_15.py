'''
Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.
'''

from questao_15_historia import *

print(f'\033[1m{titulo}\033[0m')
print(historia)

while True:
    #PARTE 1
    print(f'\n\033[1m{titulo_parte_1}\033[0m')
    print(historia_parte_1 + "\n")
    while True:
        print(parte_1_opcao_a)
        print(parte_1_opcao_b)
        parte_1_opcao = input(f'{pergunta} ')

        if(parte_1_opcao == 'a' or parte_1_opcao == 'b'):
            break
        else:
            print('Opção inexistente.\n')
    
    #PARTE 2
    if(parte_1_opcao == 'b'):
        print('Fim: Você decidiu não iniciar sua jornada.')
        break
    elif(parte_1_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_2}\033[0m')
        print(historia_parte_2 + "\n")
        while True:
            print(parte_2_opcao_a)
            print(parte_2_opcao_b)
            parte_2_opcao = input(f'{pergunta} ')

            if(parte_2_opcao == 'a' or parte_2_opcao == 'b'):
                break
            else:
                print('Opção inexistente.\n')

    #PARTE 3
    if(parte_2_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_3_a}\033[0m')
        print(historia_parte_3_a + "\n")
        while True:
            print(parte_3_a_opcao_a)
            print(parte_3_a_opcao_b)
            parte_3_opcao = input(f'{pergunta} ')

            if(parte_3_opcao == 'a' or parte_3_opcao == 'b'):
                break
            else:
                print('Opção inexistente.\n')
    elif(parte_2_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_3_b}\033[0m')
        print(historia_parte_3_b + "\n")
        while True:
            print(parte_3_b_opcao_a)
            print(parte_3_b_opcao_b)
            parte_3_opcao = input(f'{pergunta} ')

            if(parte_3_opcao == 'a' or parte_3_opcao == 'b'):
                break
            else:
                print('Opção inexistente.\n')
    
    #PARTE 4
    if(parte_2_opcao == 'a' and parte_3_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_4_a}\033[0m')
        print(historia_parte_4_a + "\n")
        while True:
            print(parte_4_a_opcao_a)
            print(parte_4_a_opcao_b)
            parte_4_opcao = input(f'{pergunta} ')

            if(parte_4_opcao == 'a' or parte_4_opcao == 'b'):
                break
            else:
                print('Opção inexistente.\n')
    elif(parte_2_opcao == 'a' and parte_3_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_4_b}\033[0m')
        print(historia_parte_4_b + "\n")
        continue
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_4_c}\033[0m')
        print(historia_parte_4_c + "\n")
        while True:
            print(parte_4_c_opcao_a)
            print(parte_4_c_opcao_b)
            parte_4_opcao = input(f'{pergunta} ')

            if(parte_4_opcao == 'a' or parte_4_opcao == 'b'):
                break
            else:
                print('Opção inexistente.\n')
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_4_d}\033[0m')
        print(historia_parte_4_d + "\n")
        while True:
            print(parte_4_d_opcao_a)
            print(parte_4_d_opcao_b)
            print(parte_4_d_opcao_c)
            parte_4_opcao = input(f'{pergunta} ')

            if(parte_4_opcao == 'a' or parte_4_opcao == 'b' or parte_4_opcao == 'c'):
                break
            else:
                print('Opção inexistente.\n')
    
    #PARTE 5
    if(parte_2_opcao == 'a' and parte_3_opcao == 'a' and parte_4_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_5_a}\033[0m')
        print(historia_parte_5_a + "\n")
        print(resultado_parte_5_a)
        break
    elif(parte_2_opcao == 'a' and parte_3_opcao == 'a' and parte_4_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_5_b}\033[0m')
        print(historia_parte_5_b + "\n")
        print(resultado_parte_5_b)
        break
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'a' and parte_4_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_5_c}\033[0m')
        print(historia_parte_5_c + "\n")
        while True:
            print(parte_5_c_opcao_a)
            print(parte_5_c_opcao_b)
            parte_5_opcao = input(f'{pergunta} ')

            if(parte_5_opcao == 'a' or parte_5_opcao == 'b'):
                break
            else:
                print('Opção inexistente.\n')
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'a' and parte_4_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_5_d}\033[0m')
        print(historia_parte_5_d + "\n")
        print(resultado_parte_5_d)
        break
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'b' and parte_4_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_5_e}\033[0m')
        print(chave_dourada + "\n")
        print(resultado_chave_dourada)
        break
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'b' and parte_4_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_5_e}\033[0m')
        print(chave_prateada + "\n")
        print(resultado_chave_prateada)
        break
    elif(parte_2_opcao == 'b' and parte_3_opcao == 'b' and parte_4_opcao == 'c'):
        print(f'\n\033[1m{titulo_parte_5_e}\033[0m')
        print(chave_bronze + "\n")
        print(resultado_chave_bronze)
        break

    #PARTE 6
    if(parte_5_opcao == 'a'):
        print(f'\n\033[1m{titulo_parte_6_a}\033[0m')
        print(historia_parte_6_a + "\n")
        print(resultado_parte_6_a)
        break
    elif(parte_5_opcao == 'b'):
        print(f'\n\033[1m{titulo_parte_6_b}\033[0m')
        print(historia_parte_6_b + "\n")
        print(resultado_parte_6_b)
        break
