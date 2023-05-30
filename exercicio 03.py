#faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

n1 = int(input('digite um numero:'))

if(n1 >=  0):
    print('\033[4;30;42mo valor é positivo!\033[m')
elif(n1 < 0):
    print('\033[4;30;41mo valor é negativo!\033[m')

print('\033[4;30;47m--FIM--\033[m')
