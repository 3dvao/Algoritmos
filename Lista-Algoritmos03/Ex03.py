a, b, ano = 80000, 200000, 0
cresA, cresB = 0.03, 0.015

while a < b:
    a += a * cresA
    b += b * cresB
    ano += 1
print('A irá ultrapassa ou igualar a população de B em {} anos.'.format(ano))
print('População A: {:.0f}'.format(a))
print('População B: {:.0f}'.format(a))
