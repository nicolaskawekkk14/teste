import usuariosdw
print('SERTÃO LIVRE')

comerciantes = []
login_atual = None

while True:
    print('\n      MENU      \n')
    print("1 - Realizar Cadastro")
    print("2 - Módulo de gerenciamento do produto e informações do vendedor")
    print('3 - Menu Cliente')
    print("0 - Sair")

    alt = input("Digite a opção desejada: ")

    if alt == "1":
        nome = (input("Digite o nome do vendedor: "))
        login = (input("Digite o login do vendedor: "))
        senha = (input("Digite a senha do vendedor: "))
        usuariosdw.realizar_cadastro(nome, login, senha, comerciantes)

    elif alt == "2":
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        logado, login_atual = usuariosdw.fazer_login(login, senha, comerciantes)

        if logado:
            while True:
                print("\nMENU DE GERENCIAMENTO DE PRODUTOS:")
                print("1 - Atualizar senha")
                print("2 - Cadastrar produto")
                print("3 - Remover produto")
                print("4 - Buscar produto")
                print("5 - Editar produto")
                print("0 - Voltar")

                opcao_gerenciamento = input("Digite a opção desejada: ")

                if opcao_gerenciamento == "1":
                    login_redefinir = input("Digite o login do vendedor: ")
                    nova_senha = input("Digite a nova senha: ")
                    usuariosdw.atualizar_senha(login_redefinir, nova_senha, comerciantes)

                elif opcao_gerenciamento == "2":
                    codigo = input("Digite o código do produto: ")
                    nome = input("Digite o nome do produto: ")
                    descricao = input('Digite a descrição do produto: ')
                    quantidade = int(input('Digite a Quantidade de produtos que deseja cadastrar: '))
                    preco = input('Digite o preço do produto: ')
                    usuariosdw.cadstrar_produto(codigo, nome, descricao, quantidade, preco, comerciantes, login_atual)

                elif opcao_gerenciamento == "3":
                    codigo = input("Digite o código do produto a ser removido: ")
                    usuariosdw.remover_produto(codigo, comerciantes, login_atual)

                elif opcao_gerenciamento == "4":
                    codigo = input("Digite o código do produto a ser buscado: ")
                    usuariosdw.buscar_produto(codigo, comerciantes, login_atual)

                elif opcao_gerenciamento == "5":
                    codigo = input("Digite o código do produto a ser atualizado: ")
                    usuariosdw.editar_produto(codigo, comerciantes, login_atual)

                elif opcao_gerenciamento == "0":
                    break

                else:
                    print("Opção inválida. Digite novamente.")

        else:
            print('usuario ou senha invalida. Digite novamente')



    elif alt == "0":
        break

    elif alt == '3':
        while True:
            print("\n MENU CLIENTE:")
            print('1 - Buscar produto ')
            print('2 - Comprar produto ')
            print('3 - Lista de compras realizadas ')
            print('4 - Consultar descrição do produto ')
            print('0 - sair')

            opcao_cliente = input('Escolha uma alternativa: ')

            if opcao_cliente == '1':
                buscar = input('Digite o nome ou a descrição do produto a ser buscado: ')
                usuariosdw.buscar_produto_cliente(comerciantes, login_atual, buscar)

            if opcao_cliente == '2':
                comprar_produto = input('Digite o nome do produto que deseja comprar: ')
                quantidade_de_produtos = int(input('Quantos produtos deseja comprar? '))
                while quantidade_de_produtos <= 0:
                    quantidade_de_produtos = int(input('a quantidade deve ser maior que 0, digite novamente: '))
                usuariosdw.comprar_produtos(comerciantes, login_atual, comprar_produto, quantidade_de_produtos)

            if opcao_cliente == '3':
                usuariosdw.lista_de_compras(login_atual)

            if opcao_cliente == '4':
                nome_produto = input('Digite o nome do produto para ver sua descrição: ')
                usuariosdw.consultar_descricao(comerciantes, login_atual, nome_produto)

            if opcao_cliente == '0':
                break

















