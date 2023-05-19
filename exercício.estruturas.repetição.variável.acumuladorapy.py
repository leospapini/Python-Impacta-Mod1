# dados diversos números inteiros, exibir
# a média dos números lidos, a entrada
# termina com a leitura do número -1 que
# não deve ser contabilizada

soma = 0
qtd = 0

n = int(input('Digite um número: '))

while n > 0:
    soma += n
    qtd += 1
    n = int(input('Digite outro número: '))

rint(f'Média dos números digitados {soma/qtd}')

#enquanto digitarmos um valor positivo, ou seja, maior q 0, a repetição
#continuará somando esses números na variável soma, e contando a quantidade de
#números na variável qtd, caso o usuário digite um número negativo
#o código pegará o resultado de todas as somas e dividirá pelo numero
#da variável qtd, ou seja, descobrirá a média entre eles
