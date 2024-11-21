'''
Faça um programa que leia um nome e sobrenome na mesma linha. 
O programa deverá exibir o nome no formato “SOBRENOME, Nome”. 
Exemplo: O nome “Maria Maia”, deverá ser apresentado como “MAIA, Maria”.
'''

def formatar_nome():
    nome_completo = input('Digite seu nome e sobrenome: ')
    nome = nome_completo.split(' ')
    print(f'{nome[-1].upper()}, {nome[0].capitalize()}')

formatar_nome()