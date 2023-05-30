#covertendo binario para decimal

binario = '111010011'
decimal = 0
expoente = 0

for digito in reversed(binario):
    decimal += int(digito) * (2 ** expoente)
    expoente += 1

print(decimal)


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

#convertendo octal para decimal

numero_octal = '167'
decimal = 0
expoente = 0

for digito in reversed(numero_octal):
    digito_int = ord(digito) - 48
    decimal += digito_int * (8 ** expoente)
    expoente += 1

print(decimal)


#conversao de hexadecimal para decimal ex:

hexadecimal = '7F8A'
hex_map = { '0': 0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

decimal = 0
for i, digit in enumerate(reversed(hexadecimal)):
    decimal += hex_map[digit] * (16 ** i)

print(decimal)


#decimal para hexadecimal ex :

numero_decimal = 543
hexadecimal = ''
hex_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

while numero_decimal > 0:
    resto = numero_decimal % 16
    if resto >= 10:
        resto = hex_map[resto]
    hexadecimal = str(resto) + hexadecimal
    numero_decimal //= 16

print(hexadecimal)



