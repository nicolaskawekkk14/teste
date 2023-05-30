for i in range(10):
    peso = float(input('digite seu peso, por favor!'))
    altura = float(input('digite sua altura também, por favor! '))

    imc = peso / (altura**2)

    if(imc < 30):
        menor = imc

        print(f'o imc foi {imc}')

    if(imc > 30):
        print('\033[4;30;41mvoce precisa ir ao médico\033[m')

    else:
        print('\033[4;30;42mvoce está saudável\033[m')
