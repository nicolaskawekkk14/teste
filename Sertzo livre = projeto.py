print(('-' * 12),'SERTÃO LIVRE','-' * 12)

# cadastrar vendedor

vendedores = {}
produtos = {}
cadastrado = ()

while True:
          print('     MENU     ')
print('1- realizar cadastro')
print('2- fazer login')
alt = int(input('realizar cadastro ou fazer login'))

          if alt == 1:
             cadastrado []
             nome = str(input('digite seu nome completo:'))
             cadastrado.append(nome)
             email = str(input('digite seu email:'))
             cadastrado.append(email)
             ano = int(input('digite seu ano de nascimento:'))
             cadastrado.append(ano)
             cpf = int(input('digite seu cpf:'))
             cadastrado.append(cpf)
             tel = int(input('digite seu telefone:'))
             cadastrado.append(tel)
             login = str(input('digite seu login:'))
             senha = str(input('digite sua senha:'))
             cadastrado.append(senha)
             comerciante[login] = cadastro
             print(comerciante)

print('   CADASTRO REALIZADO    ')

if alt == 2:
    login = str(input('digite o nome do usuario:'))
    cadastrado.append(login)
    senha = str(input('digite uma senha:'))
    cadastrado.append(senha)

    for login in comerciante:
        print('usuario ja cadastrado. tente novamente.')

    else:
        print('usuario cadastrado com sucesso!')

    while True:
        print('    MENU    ')
        print('Gerenciamento de produto')
        print('1 - cadastrar produto')
        print('2 - editar')
        print('3 - pesquisar')
        print('4 - remover produto')
        print('5 - atualizar senha do usuario')
        alt = int(input('escolha uma alternativa: '
















