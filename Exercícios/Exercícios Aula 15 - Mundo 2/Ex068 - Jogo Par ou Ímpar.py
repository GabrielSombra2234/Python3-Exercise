#Bibliotécas
from time import sleep
from random import randint

#Números
numero_aleatorio = randint(0, 10)
cont = 0
resultado = ' '

#Prints
print('=' * 35)
sleep(0.7)
print('Jogo: Par ou Ímpar!')
sleep(0.7)
print('=' * 35)
sleep(0.7)

#While e If
while True:
    #Inputs
    numero_teste = int(input('Digite um número: '))
    acao_teste = str(input('Jogue: Par ou Ímpar [P/I]: ')).upper()

    #Variaveis
    soma_resultado = numero_teste + numero_aleatorio
    resultado_pi = soma_resultado % 2

    #Verificação
    if acao_teste == 'P':
        if resultado_pi == 0:
            resultado = 'PAR'
            cont += 1
            print('O Jogador venceu!')
        else:
            print('O computador venceu!')

    #Resultado
    print('=' * 35)
    print(f'O Jogador jogou {numero_teste} e o Computador {numero_aleatorio}!')
    print(f'O resultado {soma_resultado}, e é {resultado}!')
    print('=' * 35)
    break

    if acao_teste == 'I':
        if resultado_pi == 1:
            resultado = 'ÍMPAR'
            cont += 1
            print('O Jogador venceu!')
        else:
            print('O Computardor venceu!')

    #Resultado
    print('=' * 35)
    print(f'O Jogador jogou {numero_teste} e o Computador {numero_aleatorio}!')
    print(f'O resultado {soma_resultado}, e é {resultado}!')
    print('=' * 35)
    break

print(f'O jogo terminou com {cont} vitórias para o jogador.')
print('-FIM-')
