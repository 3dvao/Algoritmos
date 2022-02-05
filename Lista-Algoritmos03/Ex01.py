nota = int(input('Digite uma nota entre 0 e 10: '))
while nota > 10:
    print('Nota invalida!')
    nota = int(input('Digite uma nota entre 0 e 10: '))
if nota <= 10:
    print('Nota válida!')
