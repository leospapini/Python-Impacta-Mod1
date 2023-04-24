print('estruturas de seleção')


#estruturas de seleção
#Concatenação(+)
#'olá' + 'mundo!' = 'olá mundo!' "somamos" as palavras
#Repetição(*)
#3 * 'w' ou 'w' * 3 = 'www' "multiplicamos" as palavras *só funciona com numero inteiro
#Comparação: operadores relacionas: ==, !=, >, >=, <, <=
#baseado em UNICODE
#Formatação:
#f-strings (formated strings)

#flags booleanas
#variáveis que guardam o resultado de uma EXPRESSÃO relacional ou lógica

idade = int(input('Qual a sua idade? '))
maior_de_idade = idade >= 18

if maior_de_idade:
    print('Você é maior de idade.')
else:
    print('Ainda é menor de idade.')

#neste exemplo utilizamos uma variável *maior_de_idade* para
#realizar uma expressão aonde o computador checa se o número digitado é
#maior ou igual a 18. mas mantemos esse resultado dentro da variável para depois
#apenas utilizarmos a variável em si dentro da condição, e não a expressão inteira.


    

