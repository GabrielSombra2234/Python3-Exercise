th1=str(input('Digite seu nome completo: ')).strip().title()
th2=th1.split()
print('Prazer em te conheçer...')
print('Seu primeiro nome é: {}.'.format(th2[0]))
print('Seu último nome é: {}.'.format(th2[len(th2)-1]))
