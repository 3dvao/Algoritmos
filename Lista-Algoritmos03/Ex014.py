num = int(input('Digite um número: '))
tot = 0
for c in range(2, num, 1):
    if num % c == 0:
        tot += 1
if tot == 0:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo'.format(num))