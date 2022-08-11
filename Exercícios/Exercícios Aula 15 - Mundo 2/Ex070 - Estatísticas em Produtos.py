# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Módulos
from time import sleep
import math

# Apresentação
print('=' * 51)
sleep(0.7)
print('| Bem vindo ao Super Mercado Guanabara!           |')
sleep(0.7)
print('-' * 51)
sleep(0.7)
print('| Digite as informações dos produdutos comprados! |')
sleep(0.7)
print('=' * 51)
sleep(0.7)

# Váriaveis
# While e Lógica
while True:
    # Carrinho de compras
    produtoComprado = str(input('Digite o nome do produto comprado: ')).capitalize()
    precoProduto = int(input('Digite o preço do produto comprado: R$'))
    condicaoContinuar = str(input('Adicionar mais produtos ao carrinho? [S/N]: ')).upper()
    
    # Colocar mais compras no carrinho
    if condicaoContinuar == 'S':
        produtoComprado = str(input('Digite o nome do produto comprado: ')).capitalize()
        precoProduto = int(input('Digite o preço do produto comprado: R$'))


# Finalização 
