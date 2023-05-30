"""
Desenvolva um programa pedindo o valor do litro da gasolina e o valor do litro do
álcool (etanol). O etanol vale a pena quando custar até 70% do valor da gasolina. O
programa deve informar com qual combustível é mais compensatório abastecer.

"""

gasol = float(input('digite o valor do litro da gasolina'))
etanol = float(input('digite o valor do litro do etanol'))

if(etanol >= gasol * 0.7):
    print('coloque gasolina')
else:
    print('coloque alcool')

