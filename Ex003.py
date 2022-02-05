valor_empretimo = float (input('Qual o valor do emprestimo? R$'))
atraso_dias = int (input('Quantos dias está em atraso?'))
multa = 0.25
valor_multa = valor_empretimo + (atraso_dias * multa)
print('O valor da multa por atraso é de: R$',valor_multa,)