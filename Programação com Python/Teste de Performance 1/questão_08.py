'''
Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.
'''
try:
    idade = int(input('Digite a sua idade: '))

    if(idade < 18):
        print('Menor de idade')
    else:
        print('Maior de idade')
except:
    print('Valor não numérico digitado.')