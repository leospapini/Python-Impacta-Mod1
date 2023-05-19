#crie um programa q solicite ao usuário
#um número natural e exiba a sequência
#crescente de zero até o número dado,
#somente os números pares.

n = int(input('Número: '))

for i in range(0, n+1, 2):
    print(i, end=' ')
