

def realizar_cadastro(nome, login, senha, comerciantes):
    if any(comerciante['login'] == login for comerciante in comerciantes):
        print('Esse login já existe. Por favor, cadastrar outro.')
    else:
        comerciante = {"nome": nome, "login": login, "senha": senha, "produto": [], "produtos_comprados":[]}
        comerciantes.append(comerciante)
        print("Comerciante cadastrado com sucesso!")



def fazer_login(login, senha, comerciantes):
    logado = False
    login_atual = None
    for comerciante in comerciantes:
        if comerciante['login'] == login and comerciante['senha'] == senha:
            print("Login realizado com sucesso!")
            login_atual = comerciante
            logado = True
            break
    return logado, login_atual

def atualizar_senha(login_redefinir, nova_senha, comerciantes):
        for comerciante in comerciantes:
            if comerciante['login'] == login_redefinir:
                comerciante['senha'] = nova_senha
                print("Senha atualizada com sucesso!")
                break
        else:
            print("Comerciante não encontrado.")

def cadstrar_produto(codigo, nome, descricao, quantidade, preco, comerciantes, login_atual):
    produto = {"codigo": codigo, "nome": nome, 'descricao': descricao, 'preco': preco, 'quantidade': quantidade}
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual['login']:
            comerciante["produto"].append(produto)
            print("Produto cadastrado com sucesso!")
            break

def remover_produto(codigo, comerciantes, login_atual):

    for comerciante in comerciantes:
        if comerciante["login"] == login_atual['login']:
            for produto in comerciante["produto"]:
                if produto["codigo"] == codigo:
                    comerciante["produto"].remove(produto)
                    print("Produto removido com sucesso!")
                    break

    else:
        print("Produto não encontrado.")

def buscar_produto(codigo, comerciantes, login_atual):
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual['login']:
            for produto in comerciante["produto"]:
                if produto["codigo"] == codigo:
                    print(f"Código: {produto['codigo']}")
                    print(f"Nome: {produto['nome']}")
                    return

            else:
                print("Produto não encontrado.")
                break

def editar_produto(codigo, comerciantes, login_atual):
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual['login']:
            for produto in comerciante["produto"]:
                if produto["codigo"] == codigo:
                    novo_nome = input("Digite o novo nome do produto: ")
                    produto["nome"] = novo_nome
                    print("Produto atualizado com sucesso!")
                    break

            else:
                print("Produto não encontrado.")
                break

def buscar_produto_cliente(comerciantes, login_atual, buscar ):
    produto_achado = False

    for comerciante in comerciantes:
        #if comerciante["login"] == login_atual['login']:
            for produto in comerciante["produto"]:
                if produto["nome"] == buscar or produto['descricao'] == buscar:
                    produto_achado = True
                    print(f"Nome: {produto['nome']}")
                    print(f"Descrição: {produto['descricao']}")
                    print(f'Quantidade: {produto["quantidade"]}')
                    produto_achado = True
                    return

    else:
        print("Produto não encontrado.")

def comprar_produtos(comerciantes, login_atual, comprar_produto, quantidade_de_produtos):
    produto_localizado = False

    for comerciante in comerciantes:
            for produto in comerciante["produto"]:
                if produto["nome"] == comprar_produto:
                    print(f"Nome: {produto['nome']}")
                    print(f"Esse produto custa: {produto['preco']}R$")
                    print(f"A quantidade é: {produto['quantidade']}")
                    if quantidade_de_produtos <= produto['quantidade']:
                        produto['quantidade'] -= quantidade_de_produtos
                        print('Forma única de pagamento: Cartão de crédito')
                        numero_cartao = int(input('Digite o número do cartão: '))
                        print('Compra realizada com sucesso!')
                        login_atual["produtos_comprados"].append(produto)
                    else:
                        print('Quantidade solicitada maior do que a disponível em estoque.')

                    produto_localizado = True
                    return

    if not produto_localizado:
        print('Produto não encontrado.')

def lista_de_compras(login_atual):
    produtos_comprados = login_atual["produtos_comprados"]


    if len(produtos_comprados) > 0:
        print("Produtos comprados:")
        for produto in produtos_comprados:
            print(produtos_comprados)
            return
    else:
        print("Nenhum produto foi comprado.")


def consultar_descricao(comerciantes, login_atual, nome_produto):
    produto_encontrado = False

    for comerciante in comerciantes:
            for produto in comerciante["produto"]:
                if produto["nome"] == nome_produto:
                    print(f"Descrição: {produto['descricao']}")
                    produto_encontrado = True
                    return

    if not produto_encontrado:
        print("Nenhum produto encontrado.")



