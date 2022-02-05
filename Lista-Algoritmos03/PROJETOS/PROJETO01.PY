cont, cont2, s = 0, 0, 0
for n in range(1, 6):
    nota = int(input('{}ª nota: '.format(n)))
    s += nota
    if n == 1:
        cont = nota
        cont2 = nota
    else:
        if nota > cont:
            cont = nota
        if nota < cont2:
            cont2 = nota
soma = cont + cont2 
resultado = (s - soma) / 3
print(resultado)
