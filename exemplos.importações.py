## Funções
def pede_idade(mensagem):
    """
    Função q pede a idade do usuário
    """
    ## colocar """ texto """ dentro de uma função ajuda a lembrar
    ## para q serve esta função caso exista dúvidas no decorrer do código
    idade = int(input(mensagem))
    return idade
## dividir o código com as importações, funções e código principal
## ajuda muito a manter a organização


## Main

idade = pede_idade('digite sua idade: ')
maior_de_idade = idade >= 18

if maior_de_idade:
    print('você é maior de idade')
else:
    print('você ainda não é menor de idade')

print('fim')    

