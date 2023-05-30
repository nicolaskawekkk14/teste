login = input(' digite o login do usuario')
senha = input(' digite a senha do usuario')

while(login == senha):
    print('erro!!!')
    login = input(' digite o login do usuario novamento')
    senha = input(' digite a senha do usuario novamente')

print(' agora voce acertou!!!')