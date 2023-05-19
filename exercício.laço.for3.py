#crie um programa q solicite ao usuário
#um número natural e exiba a sequência
#decrescente do número dado até um.

n = int(input('Número: '))

for i in range(n, 0, -1):
        print(i, end=' ')
