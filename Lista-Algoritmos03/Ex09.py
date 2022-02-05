num = int(input('Qual tabuada entre a de 1 e a 10 você pretende ver? '))
for tabu in range(1, 11):
    tabu1 = num * tabu
    print('{} X {} = {}'.format(num, tabu, tabu1))