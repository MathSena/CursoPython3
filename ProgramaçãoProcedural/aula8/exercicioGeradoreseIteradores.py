carrinho = []

carrinho.append(('Café', 1))
carrinho.append(('Açucar', 2))
carrinho.append(('Chá', 3))

total = sum([float(y) for x,y in carrinho])
print(total)