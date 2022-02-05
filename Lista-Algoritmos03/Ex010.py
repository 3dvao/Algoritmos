pot, cont = 1 , 1
num1 = int(input('Digite a base: '))
num2 = int(input('Digite o expoente: '))
while cont <= num2:
    pot = pot * num1
    cont = cont + 1
print('{} ** {} = {}'.format(num1, num2, pot))