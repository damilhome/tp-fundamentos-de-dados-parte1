'''
Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, 
convertendo horas e minutos de volta para minutos totais.
'''

#Convertendo minutos para horas e minutos
total_em_minutos_para_converter = int(input('Digite os minutos para converter para horas e minutos: '))

total_horas = total_em_minutos_para_converter // 60
total_minutos = total_em_minutos_para_converter % 60

print(f'{total_em_minutos_para_converter} minutos = {total_horas} horas e {total_minutos} minutos')

#Convertendo horas e minutos em minutos
horas_para_converter = int(input('Digite as horas (somente horas) para converter em minutos: '))
minutos_para_converter = int(input('Digite os minutos dessa hora para converter em minutos: '))

total_convertido_para_minutos = (horas_para_converter * 60) + minutos_para_converter

print(f'{horas_para_converter} horas {minutos_para_converter} minutos = {total_convertido_para_minutos} minutos')