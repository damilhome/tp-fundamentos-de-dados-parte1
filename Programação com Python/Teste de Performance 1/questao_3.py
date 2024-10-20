'''
Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.
'''

nome_1 = input('Digite um nome: ')
nome_2 = input('Digite outro nome: ')

quantidade_caracteres_nome_1 = len(nome_1)
quantidade_caracteres_nome_2 = len(nome_2)

#Pega a primeira metade do primeiro nome e concatena com a segunda metade do segundo nome
novo_nome_1 = nome_1[0:(quantidade_caracteres_nome_1 // 2)] + nome_2[(quantidade_caracteres_nome_2 // 2):quantidade_caracteres_nome_2]
#Pega a primeira metade do segundo nome e concatena com a segunda metade do primeiro nome
novo_nome_2 = nome_2[0:(quantidade_caracteres_nome_2 // 2)] + nome_1[(quantidade_caracteres_nome_1 // 2):quantidade_caracteres_nome_1]

print(f'Novo nome: {novo_nome_1}')
print(f'Novo nome: {novo_nome_2}')