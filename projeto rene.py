from usuariosdw import *
print(('-' * 12),'SERTÃO LIVRE',('-' * 12))

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
                nova_senha = input("Digite a nova senha: ")
                for comerciante in comerciantes:
                    if comerciante["login"] == login_atual:
                        comerciante["senha"] = nova_senha
                        print("Senha atualizada com sucesso!")
                        break

            elif opcao_gerenciamento == "2":
                codigo = input("Digite o código do produto: ")
                nome = input("Digite o nome do produto: ")
                produto = {"codigo": codigo, "nome": nome}
                for comerciante in comerciantes:
                    if comerciante["login"] == login_atual:
                        comerciante["produtos"].append(produto)
                        print("Produto cadastrado com sucesso!")
                        break


            elif opcao_gerenciamento == "3":
                codigo = input("Digite o código do produto a ser removido: ")
                for comerciante in comerciantes:
                    if comerciante["login"] == login_atual:
                        for produto in comerciante["produtos"]:
                            if produto["codigo"] == codigo:
                                comerciante["produtos"].remove(produto)
                                print("Produto removido com sucesso!")
                                break
                        else:
                            print("Produto não encontrado.")
                        break

            elif opcao_gerenciamento == "4":
                codigo = input("Digite o código do produto a ser buscado: ")
                for comerciante in comerciantes:
                    if comerciante["login"] == login_atual:
                        for produto in comerciante["produtos"]:
                            if produto["codigo"] == codigo:
                                print(f"Código: {produto['codigo']}")
                                print(f"Nome: {produto['nome']}")
                                break
                        else:
                            print("Produto não encontrado.")
                            break

            elif opcao_gerenciamento == "5":
                codigo = input("Digite o código do produto a ser atualizado: ")
                for comerciante in comerciantes:
                    if comerciante["login"] == login_atual:
                        for produto in comerciante["produtos"]:
                            if produto["codigo"] == codigo:
                                novo_nome = input("Digite o novo nome do produto: ")
                                produto["nome"] = novo_nome
                                print("Produto atualizado com sucesso!")
                                break
                        else:
                            print("Produto não encontrado.")
                        break

            elif opcao_gerenciamento == "0":
                break

            else:
                print("Opção inválida. Digite novamente.")

            elif alt == "0":
            break
