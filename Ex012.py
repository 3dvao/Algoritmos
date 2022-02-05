n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é {}'.format(media))
if media >= 7:
    print('Aprovado.')
elif media < 4:
    print('Reprovado.')
else:
    print('Prova Final.')
