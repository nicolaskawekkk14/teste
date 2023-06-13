from itertools import product
from sympy.logic.boolalg import And, Or, Nand
from sympy.abc import A, B, C


def tabela_verdade(expressao):
    variaveis = list(expressao.free_symbols)
    linhas = list(product([0, 1], repeat=len(variaveis)))

    tabela = []
    for valores in linhas:
        contexto = dict(zip(variaveis, valores))
        resultado = expressao.subs(contexto)
        tabela.append((valores, resultado))

    return tabela

expressao = And(A, Or(B, C, Nand(A, B)))

tabela = tabela_verdade(expressao)

print("Tabela Verdade:")
for entrada, resultado in tabela:
    entrada_formatada = ' '.join([str(valor) for valor in entrada])
    print(f"{entrada_formatada} => {resultado}")

entrada_especifica = (True, False, True)
contexto_especifico = dict(zip((A, B, C), entrada_especifica))
resultado_especifico = expressao.subs(contexto_especifico)
print(f"O Resultado para a entrada é {entrada_especifica}: {resultado_especifico}")

print('\033[7;42mtabela da verdade concluida!\033[m')
