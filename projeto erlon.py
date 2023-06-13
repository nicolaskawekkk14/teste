from sympy.logic.boolalg import truth_table
from sympy import symbols, And, Or, Nand

print('Tabela Verdade: ')
def Tabela_Verdade(expressao):
    variaveis = set()
    for atom in expressao.atoms(symbols):
        variaveis.add(atom)
    return len(variaveis)

expressao = And(Nand(symbols('A'), symbols('B')), Or(symbols('C'), symbols('A')))
total_variaveis = Tabela_Verdade(expressao)

tabela_verdade = truth_table(expressao, variables=symbols('A B C'))
print("--A--B--C = True ou false ")
for sympy in tabela_verdade:
    print(sympy)

resultado = expressao.subs([(symbols('A'), True), (symbols('B'), False), (symbols('C'), True)])
print("Resultado:", resultado)









