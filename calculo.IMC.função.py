def calculaIMC(p, a):
    imc=float
    imc=p/a**2
    return(imc)

peso=float(input('Digite o peso: '))
altura=float(input('Digite a altura: '))

R=calculaIMC(peso, altura)

print('IMC = ', R)

# não sei se este exemplo está completamente certo, fiz com base nos ensinamentos
# da aula de lógica de programação
