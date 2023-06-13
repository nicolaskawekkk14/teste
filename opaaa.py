from usuariosdw import *
print('SERTÃO LIVRE')

comerciantes = []
login_atual = None


while True:
    print('\n      MENU      \n')
    print("1 - Realizar Cadastro")
    print("2 - Módulo de gerenciamento do produto e informações do vendedor")
    print("0 - Sair")

    alt = input("Digite a opção desejada: ")

    if alt == "1":
        realizar_cadastro(comerciantes)


    elif alt == "2":
       if realizar_login(comerciantes):
           continue

    else:
        print("Login ou senha inválidos.")

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
                atualizar_senha(login_atual, comerciantes)

            elif opcao_gerenciamento == "2":
                cadastrar_produto(comerciantes, login_atual)

            elif opcao_gerenciamento == "3":
                remover_produto(comerciantes, login_atual)

            elif opcao_gerenciamento == "4":
                buscar_produto(comerciantes, login_atual)

            elif opcao_gerenciamento == "5":
                editar_produto(comerciantes, login_atual)

            elif opcao_gerenciamento == "0":
                break

            else:
                print("Opção inválida. Digite novamente.")


