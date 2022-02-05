soma = 0
for i in range(6): #[elementos  = 0,1,2,3,4,5,6]
    print('Infomr o',i+1,'º valor: ',end='')
    valor = float(input())
    soma = soma + valor
med = soma / 6
print('A média entre os 6 valore é igual a {}'.format(med))