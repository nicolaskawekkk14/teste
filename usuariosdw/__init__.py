import openai

def realizar_cadastro(comerciantes):

    nome = str(input("Digite o nome do vendedor: "))
    login = str(input("Digite o login do vendedor: "))
    senha = str(input("Digite a senha do vendedor: "))
    comerciante = {"nome": nome, "login": login, "senha": senha, "produtos": []}
    comerciantes.append(comerciante)
    print("Comerciante cadastrado com sucesso!")


def realizar_login(comerciantes):
    logado = False
    login = str((input("Digite o login: ")))
    senha = str(input("Digite a senha: "))
    for comerciante in comerciantes:
        if comerciante["login"] == login and comerciante["senha"] == senha:
            login_atual = login
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
    produto = {"codigo": codigo, "nome": nome}
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

def buscar_produto(comerciantes, login_atual):
    codigo = input("Digite o código do produto a ser buscado: ")
    for comerciante in comerciantes:
        if comerciante["login"] == login_atual:
            for produto in comerciante["produtos"]:
                if produto["codigo"] == codigo:
                    print(f"Código: {produto['codigo']}")
                    print(f"Nome: {produto['nome']}")

                else:
                    print("Produto não encontrado.")
                    break

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

def consultarchatgpt(produto):
    openai.api_key = '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'

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = 'O que voce acha do' + produto +  ''
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return completion.choices[0].text



