#convertendo octal para decimal

def decimal_para_octal(decimal):
    resultado = ''
    while decimal > 0:
        resultado = str(decimal % 8) + resultado
        decimal //= 8
    return resultado

numero_decimal = 6065
numero_octal = decimal_para_octal(numero_decimal)
print(numero_octal)