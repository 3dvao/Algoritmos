fat, i = 1, 2
num = int(input('Digite um número inteiro: '))
print('{}!'.format(num),end='=')
while i <= num:
    fat *= i
    i += 1

for c in range(num, 0, -1):
    print(c,end='.')

print('= {}'.format(fat),end=' ')

