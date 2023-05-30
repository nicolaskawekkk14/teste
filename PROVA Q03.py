"""
Desenvolva um programa que leia o código de um dos itens pedidos e a quantidade
desejada de acordo com a lista abaixo. Calcule e mostre o total geral do pedido.
Especificação Código Preço
Cachorro Quente 100 R$ 1,00
Bauru Simples 101 R$ 1,30
Bauru com ovo 102 R$ 1,50
Hambúrguer 103 R$ 1,20

"""

qtd_cq = int(input('digite a quantidade de cachorros quentes'))
qtd_bs = int(input('digite a quantidade de bauru simples'))
qtd_bco = int(input('digite a quantidade de bauru com ovo'))
qtd_h = int(input('digite a quantidade de hambúrguer'))

total = (qtd_cq * 1 + qtd_bs * 1.3 + qtd_bco * 1.5 + qtd_h * 1.2)

print(f'o total foi {total}')



