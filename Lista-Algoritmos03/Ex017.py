turmas = int(input('Digite a quantidade de turmas: '))
cont, soma = 0, 0
while cont < turmas:
    alunos = int(input('Digite a quantidade de alunos para a turma: '))
    cont = cont + 1
    soma += alunos
    if alunos > 40:
        print('É IMPOSSÍVEL MAIS DE 40 ALUNOS POR TURMA') #isso ta errado :(
media = soma / turmas
print('Com {} turmas, a média de alunos por turma é {:.0f}.'.format(turmas, media))

    
