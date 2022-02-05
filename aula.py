valor = int(input('Digite um valor: '))
par = valor % 2
for valor in range(1,6,1):
    if  par == 0:
        print('Par')
    else:
        print('Impar')