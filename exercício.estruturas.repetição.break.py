#crie um programa que rebeca um número natural
#n(n>1) e exiba uma mensagem indicando se n é primo.

#BREAK é utilizado para parar o código em um momento específico ou condição
#específica.

n = int(input('Número: '))
divisor = 2

while divisor < n:
    print(f'{n} % {divisor} = {n % divisor}')
    if n % divisor == 0:
        break
    divisor += 1

if divisor==n:
    print('primo')
else:
    print('não é primo')
