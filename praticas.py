n1 = float(input('digite a primeira nota'))
n2 = float(input('digite a segunda nota'))
n3 = float(input('digite a terceira nota'))
n4 = float(input('digite a quarta nota'))

m = (n1 + n2 + n3 + n4)/4
print('a sua media é {:.1f}'.format(m))
if m >= 7.0:
    print('sua media foi boa! parabens!')
else:
    print('sua media esta baixa! estude mais!')

