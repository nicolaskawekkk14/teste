#convertendo octal para decimal

numero_octal = '167'
decimal = 0
expoente = 0

for digito in reversed(numero_octal):
    digito_int = ord(digito) - 48
    decimal += digito_int * (8 ** expoente)
    expoente += 1

print(decimal)