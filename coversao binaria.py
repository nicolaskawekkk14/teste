# Converter decimal para binario
# Jeito facil

decimal = 12

valor_em_binario = bin(decimal)
print(f"Decimal: {decimal}")
print(f"Binario: {valor_em_binario}")

# Jeito maneiro
resto = ""
while True:
    if decimal == 0:
        break
    resto_int = decimal % 2

    cociente = decimal // 2
    resto += str(resto_int)
    decimal = cociente

em_binario = resto[::-1]

print(f"Jeito maneiro - Decimal para binario: {em_binario}")

#-------------------------------
# Convertendo binario para decimal /////ja fiz
#! DESAFIO PARA A TURMA

#-------------------------------
# Convertendo decimal para octal ////// ja fiz
# Jeito facil
decimal = 285

valor_em_octal = oct(decimal)
print(f"Decimal: {decimal}")
print(f"Octal: {valor_em_octal}")

# Jeito maneiro
#! DESAFIO PARA A TURMA


#-------------------------------
# Convertendo octal para decimal
#! DESAFIO PARA A TURMA



#-------------------------------
# Convertendo decimal para hexadecimal
# Jeito facil
decimal = 285

valor_em_octal = hex(decimal)
print(f"Decimal: {decimal}")
print(f"Hexadecimal: {valor_em_octal}")

# Jeito maneiro
#! DESAFIO PARA A TURMA


#-------------------------------
# Convertendo hexadecimal para decimal
#! DESAFIO PARA A TURMA