lista = list() #ordem #armazena itens #index #mutavel
tupla = tuple() #ordem #armazena itens #index #imutavel
dicionario = dict() #desordem #armazena chave valor #mutavel

conjunto2 = {"rene", "nicolas", "gabriel", "yan"}

busca = input('digite o nome para busca')
for nome in conjunto2:
    if(nome == busca):
        conjunto2.remove(nome)
        print('a pessoa foi delatada')
        break


print(conjunto2)




#funçoes///////

