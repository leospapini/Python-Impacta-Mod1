print('Operadores relacionais')

#== igual a
#!= diferente de
#> maior que
#>= maior ou igual a
#< menor que
#<= menor ou igual a

#NÃO (vulgo not)
#E (vulgo and)
#OU (vulgo or)

#ordem de resolução
#1° ** à direita
#2° +, - (unários, identidade e negação) à esquerda
#3° *, /, //, % à esquerda
#4° +, - (binários, adição e subtração) à esquerda
#5° ==, !=, >, >=, <, <= não associados
#6° not à esquerda
#7° and à esquerda
#8° or à esquerda

#condição se declara com if <condição>:
#                               <bloco de código>
#ou no caso de "senão" if <condição>
#                           <bloco de código>
#                      else:
#                           <bloco de código>


idade = int(input('digite sua idade: '))

if idade >= 18:
    print('você é maior de idade')

else:
    print('você ainda é menor de idade')
    
print('fim')
