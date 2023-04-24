print('Praticando1')

#Crie um programa para um site! O programa deverá solicitar o valor de um item
# e a quantidade de unidades compradas deste item, ao final deve exibir o total
#com desconto de 10%. Considere que a quantidade será um número natural positivo.

valor1 = float
quantidade1 = int
multi = float
desconto = float
valor_total = float

valor1 = float(input('Digite o valor do item comprado: '))
print(valor1)

quantidade1 = int(input('Digite a quantidade de unidades do item comprado: '))
print(quantidade1)

multi = valor1*quantidade1
desconto = multi/10
valor_total = multi-desconto


print('O valor com desconto ficou: ',valor_total)
