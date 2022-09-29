# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Inicialização
print('=' * 35)
print('|{:^33}|'.format('Números por extenso'))
print('=' * 35)

# Váriaveis
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 
           'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

# While e lógica
while True:
    numeroPerguntado = int(input('Digite um numero entre 0 até 20, para ve-lo por extenso: '))
    if 0 <= numeroPerguntado <= 20:
        break
    print('\033[31mERRO! Tente novamente!\033[m') # , end=''

# Finalização
print(f'Você digitou o número \033[32m{numeros[numeroPerguntado]}\033[m!')
print('-FIM-')
