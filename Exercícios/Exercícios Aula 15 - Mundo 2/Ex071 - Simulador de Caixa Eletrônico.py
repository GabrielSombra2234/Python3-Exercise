# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro),
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# Módulos
from time import sleep

# Apresentação
print('=' * 51)
sleep(0.7)
print('|{:^49}|'.format('Bem vindo ao Banco Guanabara!'))
sleep(0.7)
print('-' * 51)
sleep(0.7)
print('|{:^49}|'.format('Digite quanto deseja sacar!'))
sleep(0.7)
print('-' * 51)
sleep(0.7)
print('|{:^49}|'.format('Notas diponiveis: R$50, R$20, R$10 e R$1!'))
sleep(0.7)
print('=' * 51)
sleep(0.7)

# Digitando o valor
valorSacado = int(input('Digite o valor a ser sacado: R$'))
print('=' * 40)

# Váriaveis
valorTotal = valorSacado
cedula = 50
totalCedula = 0

# While e Lógica
while True:
    if valorTotal >= cedula:
        valorTotal -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}!')
            print('-' * 35)
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if valorTotal == 0:
            break

# Finalização
print('-FIM-')