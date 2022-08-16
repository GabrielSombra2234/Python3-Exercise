# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Módulos
from time import sleep

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
totalCompra = acimaDeMil = cont = menorPreco = 0
menorProduto = ''

# While e Lógica
while True:
    
    # Informações do produto
    nomeProduto = str(input('Digite o nome do produto: ')).capitalize()
    precoProduto = float(input('Digite o preço do produto: R$'))
    cont += 1
    
    # Preço total e Verificação
    totalCompra += precoProduto
    if precoProduto > 1000:
        acimaDeMil += 1
    
    # Produto mais barato e Verificação
    if cont == 1 or precoProduto < menorPreco:
        menorPreco = precoProduto
        menorProduto = nomeProduto

    # Loop sim ou não
    resposta = ' '
    while resposta not in 'SN':
        print('=' * 51)
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break

# Finalização
print('=' * 51)
print(f'O total da compra foi de R${totalCompra:.2f}!')
print(f'Temos {acimaDeMil} produtos acima de R$1000.00!')
print(f'O produto mais barato foi {menorProduto}, custando R${menorPreco:.2f}!')
print('-FIM-')
