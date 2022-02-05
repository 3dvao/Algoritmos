largura_um = float (input('Digite a largura do cômodo 1:'))
comprimento_um = float (input('Digite o comprimento do cômodo 1:'))
metro_um = largura_um * comprimento_um
print('O primeiro cômodo tem:',metro_um,'m2')

largura_dois = float (input('Digite a largura do cômodo 2:'))
comprimento_dois = float (input('Digite o comprimento do cômodo 2:'))
metro_dois = largura_dois * comprimento_dois
print('O segundo cômodo tem:',metro_dois,'m2')

largura_tres = float (input('Digite a largura do cômodo 3:'))
comprimento_tres = float (input('Digite o comprimento do cômodo 3:'))
metro_tres = largura_tres * comprimento_tres
print('O segundo cômodo tem:',metro_tres,'m2')

largura_quatro = float(input('Digite a largura do cômodo 4:'))
comprimento_quatro = float (input('Digite o comprimento do cômodo 4:'))
metro_quatro = largura_quatro * comprimento_quatro
print('O segundo cômodo tem:',metro_quatro,'m2')

area_total = (largura_um + largura_dois + largura_tres + largura_quatro) * (comprimento_um + comprimento_dois + comprimento_quatro + comprimento_tres)
print('A área total da sua casa é:',area_total,'m2')