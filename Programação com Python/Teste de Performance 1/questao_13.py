'''
Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).
'''

palavra = input('Digite a palavra: ')

palindromo = palavra[::-1]

if(palavra == palindromo):
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')

