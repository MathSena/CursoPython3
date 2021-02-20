from vendas.calc_preco import aumento, reduz

preco = 49.90
preco_com_aumento = aumento(preco, 10)

print(preco_com_aumento)

preco_com_reducao = reduz(preco, 5)

print(preco_com_reducao)


