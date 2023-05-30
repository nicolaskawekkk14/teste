populaçao = 230
taxadecresc = 1.012
ano = 2023

while(populaçao <= 300):
    ano *= 1
    populaçao *= taxadecresc

quantidadesdeano = ano - 2023
mandatos = quantidadesdeano // 4

print(f' se passarem {quantidadedeanos} anos.')
print(f'foram {mandatos}  mandatos')

