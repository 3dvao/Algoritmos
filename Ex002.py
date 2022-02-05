kilometragem_inicial = float (input('Informe sua KM inicial: '))
kilometragem_final = float (input('Informe sua KM Final: '))
litro = 10
consumo_gasolina = (kilometragem_final - kilometragem_inicial) / litro
print('Seu consumo de gasolina foi de',consumo_gasolina,'L')