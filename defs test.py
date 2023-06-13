comercinates = []

def realizar_cadastro(comerciantes, login_atual):

    nome = str(input("Digite o nome do vendedor: "))
    login = str(input("Digite o login do vendedor: "))
    senha = str(input("Digite a senha do vendedor: "))
    comerciante = {"nome": nome, "login": login, "senha": senha, "produto": []}
    comerciantes.append(comerciante)
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual:
         print("Esse login já existe. Por favor digite novamente.")

        else:
            print("Comerciante cadastrado com sucesso!")


def realizar_login(comerciantes, login_atual):

    logado = False
    login = str((input("Digite o login: ")))
    senha = str(input("Digite a senha: "))
    for comerciante in comerciantes:
        if comerciante["login"] == login and comerciante["senha"] == senha:
            login = login_atual
            print("Login realizado com sucesso!")
            logado = True
            break
    return logado


def atualizar_senha(login_atual, comerciantes):

    nova_senha = input("Digite a nova senha: ")
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual:
            comerciante["senha"] = nova_senha

            print("Senha atualizada com sucesso!")
            break


def cadastrar_produto(comerciantes, login_atual):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = input("digite o preco do produto: ")
    produto = {"codigo": codigo, "nome": nome, "preco": preco}
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual:
            comerciante["produtos"].append(produto)
        print("Produto cadastrado com sucesso!")
        break


def remover_produto(comerciantes, login_atual):
    codigo = input("Digite o código do produto a ser removido: ")
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual:
            for produto in comerciante["produtos"]:
                if produto["codigo"] == codigo:
                    comerciante["produtos"].remove(produto)
                print("Produto removido com sucesso!")
                break


def buscar_produto(comerciantes, login_atual,):

    codigo = input("Digite o código do produto a ser buscado: ")
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual:
            for produto in comerciante["produtos"]:
                if produto["codigo"] == codigo:
                    print(f"Código: {produto['codigo']}")
                    print(f"Nome: {produto['nome']}")
                    return
    print("produto não encontrado.")


def editar_produto(comerciantes, login_atual):
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





