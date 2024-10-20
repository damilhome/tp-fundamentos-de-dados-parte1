'''
Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.
'''
import random

lista_personagens = ['Um cavaleiro destemido', 'Uma cientista maluca', 'Um dragão pacífico', 'Uma espiã disfarçada', 'Um robô curioso', 'Um pirata perdido', 'Uma feiticeira poderosa', 'Um astronauta aventureiro', 'Um fantasma amigável', 'Um arqueólogo corajoso']
lista_acoes = ['Descobriu um segredo antigo', 'Começou a construir uma máquina do tempo', 'Enfrentou um exército de zumbis', 'Salvou um reino em apuros', 'Encontrou um tesouro escondido', 'Inventou uma poção mágica', 'Viajou para o passado', 'Destruiu uma cidade inteira por acidente', 'Lançou um feitiço que saiu errado', 'Conduziu uma expedição para outro planeta']
lista_locais = ['Em uma floresta encantada', 'Nas profundezas de um vulcão', 'No espaço sideral', 'Em um castelo abandonado', 'Na capital de um reino distante', 'Em um laboratório subterrâneo', 'Em uma ilha deserta', 'Dentro de uma caverna misteriosa', 'No topo de uma montanha gelada', 'Em uma cidade futurista']

personagens_selecionados = []
acoes_selecionadas = []
locais_selecionados = []

for i in range(10):
    personagem_selecionado = random.randint(0, 9)
    while personagem_selecionado in personagens_selecionados:
        personagem_selecionado = random.randint(0, 9)
    personagens_selecionados.append(personagem_selecionado)

    acao_selecionada = random.randint(0, 9)
    while acao_selecionada in acoes_selecionadas:
        acao_selecionada = random.randint(0, 9)
    acoes_selecionadas.append(acao_selecionada)

    local_selecionado = random.randint(0, 9)
    while local_selecionado in locais_selecionados:
        local_selecionado = random.randint(0, 9)
    locais_selecionados.append(local_selecionado)
    
    historia = f'{lista_personagens[personagem_selecionado]} {lista_acoes[acao_selecionada]} {lista_locais[local_selecionado]}'
    print(historia)
