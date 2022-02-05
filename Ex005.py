cotacao_dolar = float (input('Informe a cotacao do dolar: U$'))
reais = float (input('Informe quantos reais voce deseja converter: R$'))

converte = reais / cotacao_dolar

print('Voce tera: U$ {:.2f},apos a conversao.'.format(converte))