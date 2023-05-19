def somatemp():
    soma = 0
    cont = 1
    while cont <= 30:
        temp=float(input('digite a temperatura: '))
        soma = soma+temp
        cont += 1
    return soma

s=somatemp()
print('A soma das temperaturas é: ', s)
