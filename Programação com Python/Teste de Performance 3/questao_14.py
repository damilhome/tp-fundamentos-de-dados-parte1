'''
Faça um programa que leia a frase abaixo e mostre os cinco primeiros e os cinco últimos caracteres, utilizando o comando [::] de manipulação de strings.
'''

FRASE = 'eu gosto de programar'

print(f'Cinco primeiros: {FRASE[:5:]}')
print(f'Cinco últimos: {FRASE[-1:-6:-1][::-1]}')