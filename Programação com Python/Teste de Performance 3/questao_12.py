'''
Faça um programa que leia a frase abaixo e mostre a frase invertida, utilizando o comando de repetição “for”. 
'''

FRASE = 'eu gosto de programar'

def mostrar_frase_invertida():
    nova_frase = ''
    for caractere in FRASE:
        nova_frase = caractere + nova_frase
    
    print(nova_frase)

mostrar_frase_invertida()