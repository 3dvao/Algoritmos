nome = str(input('Digite seu usuário: ')).upper()
senha = str(input('Digite sua senha: ')).upper()

while senha == nome:
    print('!Login Inválido! SENHA igual ou USUÁRIO!')
    senha = str(input('Digite novamente sua senha: '))
if senha != nome:
    print('Login feito com sucesso.')
    print('Seja bem-vindo!')