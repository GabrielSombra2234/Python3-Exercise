# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# E também indique o menor e o maior valor na tupla.

# Bibliotecas
from random import randint

# Variáveis
numeroSorteado = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maiorNumero = max(numeroSorteado)  # verifica o maior número.
menorNumero = min(numeroSorteado)  # verifica o menor número.

# Inicio
print(f"Os Números sorteados foram: {numeroSorteado}!")
print(f"Dos números acima, o Maior é o: {maiorNumero}! e o Menor é o: {menorNumero}!")

# Final
print("-FIM-")
