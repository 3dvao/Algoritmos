largura = float (input('Qual a largura da sala em m?'))
comprimeto = float (input('Qual o comprimento da sala em m?'))

comprimento_carteira = float(input('Informe o comprimento da carteira em m:'))
largura_carteira = float (input('Informe a largura da carteira em m:'))

quant_larg = (largura + 0.5) // (largura_carteira + 0.5) 
quant_comp = (comprimeto + 0.2 - 1.5) // (comprimento_carteira + 0.2)

quant_sala = quant_larg * quant_comp

print('Cabem',quant_sala,'carteiras na sala.')