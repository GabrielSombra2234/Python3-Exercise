#Bibliotécas
from time import sleep

#Prints
print('=-' * 10)
sleep(0.7)
print('Condição de parada')
sleep(0.7)
print('Digite 999 para sair!')
sleep(0.7)
print('=-' * 10)
sleep(0.7)

#Váriaveis
soma = cont = numeros = 0

#while and if
while True:
    numeros = int(input('Digite um número: '))
    if numeros == 999:
        break
    cont += 1
    soma += numeros
print('=-' * 10)
print(f'# O programa terminou com {cont} números digitados.\n# E a soma entre eles foi de {soma}.')
sleep(0.7)
print('-Fim-')
