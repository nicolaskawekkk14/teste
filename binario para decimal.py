#covertendo binario para decimal

binario = '111010011'
decimal = 0
expoente = 0

for digito in reversed(binario):
    decimal += int(digito) * (2 ** expoente)
    expoente += 1

print(decimal)







