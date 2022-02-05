nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2ª nota: '))
media = (nota1 + nota2) / 2
print('Sua media foi {}.'.format(media))

if media >= 7:
    print('Aprovado!')
elif media < 4:
    print('Reprovado!')
else:
    print('Prova final!')