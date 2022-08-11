#Bibliotéca
from time import sleep

#Prints
print('=-' * 12)
sleep(0.7)
print('Tabuada Digital')
sleep(0.7)
print('=-' * 12)

#While and if
while True:
    numero = int(input('Digite um número para ver a sua tabuada: '))
    print('Multiplicando...')
    sleep(0.9)
    print('-' * 18)
    if numero < 0:
        break
    for cont in range (1, 11):
        print(f'{cont} x {numero} = {numero * cont}')
        sleep(0.7)
    print('-' * 18)
print('Acabou!')
