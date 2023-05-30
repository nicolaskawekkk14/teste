for i in range(10):
    peso = float(input('digite seu peso'))
    altura = float(input('digite sua altura'))

    imc = peso / (altura**2)
    if(imc < 30):
        menor = imc

    print(f'o imc foi {imc}')


    if(imc > 30):
        print('procure um medico')
    else:
        print('vc esta saudavel')