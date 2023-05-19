#crie um programa q rebeca um número n >= 0
#e exiba o valor da raiz quadrada de n.
#enquanto n for um número negativo, repita a
#solicitação de entrada.

from math import sqrt

while True:
    n = float(input('Digite um número: '))
    if n >= 0: break

print(f'Raiz quadrada de {n} é {sqrt(n)}')
