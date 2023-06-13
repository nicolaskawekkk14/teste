from sympy.logic.boolalg import truth_table
from sympy import symbols, And, Or, Nand, sympify

def calcular_total_variaveis(expressao):
    variaveis = set()
    for atom in expressao.atoms(symbols):
        variaveis.add(atom)
    return len(variaveis)

expressao_str = "( A & B ) & ( C | A )"
expressao = sympify(expressao_str)
total_variaveis = calcular_total_variaveis(expressao)
print("Total de variáveis:", total_variaveis)

# Montar tabela verdade
tabela_verdade = truth_table(expressao, variables=symbols('A B C'))
print("Tabela Verdade:")
for substituicoes in tabela_verdade:
    resultado = expressao.subs(substituicoes)
    print(substituicoes, resultado)

# Calcular usando operadores lógicos
valores_variaveis = [(symbols('A'), True), (symbols('B'), False), (symbols('C'), True)]
resultado = expressao.subs(valores_variaveis)
print("Resultado:", resultado)


