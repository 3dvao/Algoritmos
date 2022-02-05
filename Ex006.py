valor_salario = float (input('Quanto voce ganha: R$'))
valor_reajuste = float (input('Qual a porcetagem sera acrescida?'))
reajuste = (valor_salario * valor_reajuste) / 100 + valor_salario

print('Apos o reajuste do seu salario voce passara a ganhar: R$',reajuste,)