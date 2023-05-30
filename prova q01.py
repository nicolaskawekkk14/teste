"""
Desenvolva um algoritmo em python leia 2 números e em seguida pergunte ao
usuário qual operação ele deseja realizar (soma, subtração, multiplicação ou divisão). O
programa deve exibir resultado da operação e informar se o número resultante é:
a. par ou ímpar (inteiro); b. positivo ou negativo; c. inteiro ou decimal.
"""


num1 = float(input('digite numero'))
num2 = float(input('digite numero'))

op = int(input('digite a operação desejada 1-soma 2-subtraçao 3-divisao 4-multipli'))

if(op == 1):
    resp = num1 + num2
elif(op == 2):
    resp = num1 - num2
elif (op == 3):
    resp = num1 / num2
else:
    resp = num1 * num2

if(resp % 2 == 0):
    print('par')
else:
    print('impar')

if(resp > 0):
    print('positivo')
else:
    print('negativo')

if(resp % 1 ==0):
    print('inteiro')
else:
    print('real')