#dicionario
#estrutura de dados = chave

alunos = dict()

nome = 'lkjsad'
while (nome != 'sair'):
    nome = input('digite o nome do aluno')

    if(not nome == 'sair'):
        idade = int(input('digite sua idade'))
        alunos[nome] = idade

    print(alunos)

    for chave in alunos:

        if (alunos[chave] > 25):
            print('\033[4:40:42mele é maior\033[m')
        else:
            print('\033[4;40;41mele é menor\033[m')


