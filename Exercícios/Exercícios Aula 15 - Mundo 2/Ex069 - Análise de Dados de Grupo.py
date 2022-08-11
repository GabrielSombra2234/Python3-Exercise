# Bibliotécas
from time import sleep

# Prints
print('=-' * 25)
print('Ánalise do grupo')
print('=-' * 25)

# Variáveis
masculino = feminino = cont = 0

# Condições
while True:
    # Escolhendo o sexo
    sexo = str(input('Digite o seu sexo: [F/M]: ')).upper()
    if sexo == 'M':
        masculino += 1
    idade = int(input('Digite a sua idade: '))
    print('=-' * 25)
    
    # Verificando maior idade
    if idade >= 18:
        cont += 1
    
    # Verificando feminino aos 20
    elif idade >= 20 and sexo == 'F':
        feminino += 1 
    decisao = str(input('Deseja continuar: [S/N]: ')).upper()
    print(f'=-' * 25)
    if decisao == 'N':
        break
    else:
        pass

# Resultados
print(f'Foram {cont} pessoas com mais de 18 anos cadastradas!')
print(f'Foram {masculino} homens cadastrados!')
print(f'Foram {feminino} mulheres com menos 20 anos cadastradas!')
print('--FIM--')
