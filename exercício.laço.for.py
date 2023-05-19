#crie um programa q solicite ao usuário
#um número natural e exiba a sequência
#crescente de um até o número dado.

n = int(input('Número: '))

for i in range(1, n+1): #[1..n[
    print(i, end=' ')
