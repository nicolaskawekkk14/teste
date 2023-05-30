print(('-' * 12),'SERTÃO LIVRE',('-' * 12))


comerciante = {}

dicprodutos = {123: ['carro', 4454, 'vermelho'], 456:['moto', 999, 'vermelho']}


alt =99
while alt != 0:

            print('      MENU      ')
            print('1 - Realizar cadastro')
            print('2 - fazer login')
            print('0 sair')
            alt = int(input('Escolha uma alternativa: '))

            if alt == 1:
                    cadastrado = []
                    nome = str(input('Nome completo: '))
                    cadastrado.append(nome)
                    email = str(input('E-mail: '))
                    cadastrado.append(email)
                    cpf = int(input('CPF: '))
                    cadastrado.append(cpf)
                    tel = int(input('Número de telefone: '))
                    cadastrado.append(tel)
                    login = str(input('Digite o nome de usuário: '))
                    senha = str(input('Digite uma senha: '))
                    cadastrado.append(senha)
                    comerciante[login] = cadastrado
                    print(comerciante)


            if alt == 2:
                login = str(input('Digite o nome de usuário: '))
                cadastrado.append(login)
                senha = str(input('Digite uma senha: '))
                cadastrado.append(senha)

                for login in comerciante:
                    print('Usuário já cadastrado. Tente novamente.')

                else:
                    print('Usuário cadastrado com sucesso!')

                while True:
                    print('      MENU      ')
                    print('Gerenciamento de produtos')
                    print('1 - cadastrar produto')
                    print('2 - editar')
                    print('3 - pesquisar')
                    print('4 - remover produto')
                    print('5 - Atualizar a senha de usuário')
                    print('6 sair') # fazer um elif pra quando digitar 6 vi cair no break

                    esc = int(input('Escolha uma alternativa: '))

                    if esc == 1:
                        produtos = []
                        nome = input('Digite o nome do produto: ')
                        produtos.append(nome)
                        estoque = input('Digite a quantidade em estoque do produto: ')
                        produtos.append(estoque)
                        codigo = input('Digite o codigo do produto:')
                        preco = input('Digite o preço do produto: ')
                        produtos.append(preco)
                        dicprodutos[codigo] = produtos

                    elif esc == 2:
                        busca = input('Digite o nome do produto para buscar: ')

                        for prod in dicprodutos:
                            if(dicprodutos[prod][0].find(busca) >= 0):
                                 print(f'{prod} - {dicprodutos[prod]}')

