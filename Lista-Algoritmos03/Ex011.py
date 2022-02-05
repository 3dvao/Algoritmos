par, impar = 0, 0
for n in range(1, 11):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print('Entre os números digitados {} foram pares e {} foram ímpares.'.format(par, impar))
