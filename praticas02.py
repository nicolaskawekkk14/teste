#faça um programa que peça dois numeros e imprima o maior dele

n1 = int(input('digite um numero:'))
n2 = int(input('digite o segundo numero:'))

if(n1 > n2 ):
    print("maior numero:",n1)
elif(n1 == n2):
    print("Ops ambos os numeros digitados são iguais por favor insira novamente")
elif(n1 < n2):
    print("maior numero:",n2)




