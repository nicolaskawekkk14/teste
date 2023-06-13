#from sympy import symbols
#import sympy.logic.boolalg
#from codeTruthtable import resultadoTabelaVerdade



def tabela_verdade(expressao):
     valores_para = [0, 1] #(0 = False, 1 = True)
     operadores = ['xor', 'not','and', 'or']
     expressao = 'p', 'q'
     for p in valores_para:
         for q in valores_para:
             for operadores in operadores:
                 resultado = caucular(p,q,operador)
                 print(f'{p} {operador} {q} = {resultado}')

def calcular_operadores(p, q, operador):
    if operador == 'and':
        return p and q
    elif operador == 'or':
        return p or q
    elif operador == 'xor':
        return p ^ q
    elif operador == 'not':
        return not p

tabela_verdade()






















