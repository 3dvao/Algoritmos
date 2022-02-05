'''soma, cont = 0, -1
print('Para parar o programa digite 0')
ida = int(input('Digite sua idade: ')) 
while ida > 0:
    ida = int(input('Digite sua idade: '))
    soma += ida
    cont += 1
media = soma / cont
if media >= 0 and media <= 25:
    print('Turma jovem!')
elif media >= 26 and media < 60:
    print('Turma adulta') 
else:
    print('Turma idosa!')'''

soma, cont = 0, 0
pessoas = int(input('Quantas pessoas irão participar da pesquisa? '))
while pessoas <= 0:
    print('É necessário incluir ao menos uma pessoa;')
for c in range(1, pessoas + 1):
    idade = int(input('''[ {} ] 
    DIGITE A SUA IDADE: '''.format(c)))
    soma += idade
    cont += 1
media = soma / cont
if media >= 0 and media <= 25:
    print('Média entre as idades {}. TURMA JOVEM!'.format(media))
elif media >= 26 and media < 60:
    print('Média entre as idades {}. TURMA ADULTA!'.format(media))
else:
    print('Média entre as idades {}. TURMA IDOSA!'.format(media))