n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
if n1 < n2:
    for i in range(n1,n2+1,1):
        print(i,end=' ')# o 'end' deixa o numeros em linha reta, e os espaços montam espaços entre os números
else:
    for i in range(n2,n1+1,1):
        print(i,end=' ')