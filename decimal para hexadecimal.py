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






