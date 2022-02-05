menor, maior = 0, 0
soma = 0
num = int(input('Digite um número: '))
while num != 0:
    soma += num
    if num == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('{} maior {} menor soma {}'.format(maior, menor, soma))


