cont = 0
for c in range(1, 11):
    num = int(input('Digite o {}º número: '.format(c)))
    if c == 1:
        cont = num
    else:
        if num > cont:
            cont = num 
print('O maior número digitado foi: {}'.format(cont))

