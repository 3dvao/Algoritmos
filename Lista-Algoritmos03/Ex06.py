soma = 0
for c in range(1, 11):
    num = int(input('Digite o {}º número: '.format(c)))
    if num == num:
        soma = soma + num
media = soma / 10
print('A soma entre os números digitados é {} e a média entre eles é {}'.format(soma, media))
