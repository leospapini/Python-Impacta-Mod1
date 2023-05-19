# dados dois números inteiros p (>=0) e
# q (>0), exibir o quociente da divisão
# inteira de p por q sem usar operadores
# de divisão e multiplicação (foco em estruras de repetição


p = int(input('p: '))
q = int(input('q: '))
contador = 0 #número de vezes q eu consegui subtrair p por q
             #ou seja, quantas vezes eu conseguiria dividir inteiramente
             #um número pelo outro sem q o resultado seja negativo

while p >= q:
    p = p - q # p -= q
    contador += 1

print(f'o quociente da divisão é {contador}')
