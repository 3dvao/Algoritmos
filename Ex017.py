valor_hora = float(input('Digite o valor da sua hora:R$ '))
quant_hora = int(input('Digite quantas horas trablhadas no mês: '))
salario = valor_hora * quant_hora

if salario <= 900:
    aliquota = 0
elif salario <= 1500:
    aliquota = 5
elif salario <= 2500:
    aliquota = 10
else:
    aliquota = 20
ir = salario * aliquota / 100
print('Salario bruto R$',valor_hora,'*',quant_hora, '= R$',salario,)
print('(-) IR(',aliquota,'%)             :R$',ir,sep='')
sin = salario * 3 / 100
print('(-) Sindicato (3%)                :R$',sin,sep='')
fgts = salario * 11 / 100
print('FGTS (11%)                        :R$',fgts,sep='')
desc = ir + sin
print('Total de descontos                :R$',desc,sep='')
liq = salario - desc
print('Salário Líquido                   :R$',liq,sep='')
