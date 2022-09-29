# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

# Bibliotécas
from time import sleep

# Início
print('=' * 51)
print('|{:^49}|'.format('Tabela dos 20 Primeiros Colocados - Brasileiram'))
print('=' * 51)

# Váriaveis
cont = 1
tabelaFutebol = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 
                'Athletico-PR', 'Atlético-MG', 'América-MG', 'Goiás', 'Santos',
                'Bragantino', 'Botafogo', 'São Paulo', 'Ceará', 'Fortaleza', 
                'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')

# Bloco do 5 Primeiros
print('=' * 50)
print(f'Os 5 primeiros colocados são os: {tabelaFutebol[0:5]}')
print('-' * 15)
for times in tabelaFutebol[0:5]:
    print(f'{cont}º: {times}')
    sleep(0.7)
    print('-' * 15)
    cont += 1
print('=' * 50)

# Bloco dos 4 Últimos
print(f'Os 4 últimos colocados são os: {tabelaFutebol[16:]}')
print('-' * 15)
cont =+ 17
for times in tabelaFutebol[16:]:
    print(f'{cont}º: {times}')
    sleep(0.7)
    print('-' * 15)
    cont += 1
print('=' * 50)

# Bloco da Ordem Alfabérita
print(f'Todos os 20 colocados estão aqui: {tabelaFutebol}')
sleep(0.7)
print('-' * 50)
print(f'Agora em Ordem Alfabética: {sorted(tabelaFutebol)}')
print(0.7)
print('=' * 50)

# Bloco Chapecoense
print("O 'Chapecoense' não está entre os 20 colocados!")
print('=' * 50)

# Final
print('-FIM-')
