'''
Faça um programa que leia um nome e sobrenome na mesma linha e verifique se a entrada é válida. 
Uma entrada válida é uma regra de negócio, onde o nome e o sobrenome tenham pelo menos dois caracteres. 
Utilize os comandos “split” e “len”. 

Exemplo:  “Lu Ma”. Se a entrada não for válida, exibir uma mensagem de erro e pedir ao usuário uma nova entrada para o nome.
'''

def verificar_nome():
    '''Verifica se um nome e sobrenome digitados pelo usuários são válidos, isso é, têm pelo menos 2 caracteres.'''
    nome_completo = input('Digite o nome e sobrenome: ')
    nome = nome_completo.split(' ')
    if(len(nome) < 2):
        print('Erro: Digite o nome e sobrenome.')
        return verificar_nome()
    for n in nome:
        if(len(n) < 2):
            print('Erro: nome e sobrenome devem ter pelo menos 2 caracteres.')
            return verificar_nome()
    print(nome_completo)

verificar_nome()