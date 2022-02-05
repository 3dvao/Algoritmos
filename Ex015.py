p1 = float(input('Digite o valor do 1º produto:R$ '))
p2 = float(input('Digite o valor do 2º produto:R$ '))
p3 = float(input('Digite o valro do 3º produto:R$ '))

if p1 < p2 and p1 < p3:
    print('O produto mais barato é o de R${}'.format(p1))
elif p2 < p1 and p2 < p3:
    print('O produto mais barato é o de R${}'.format(p2))
else:
    print('O produto mais barato é o de R${}'.format(p3))


