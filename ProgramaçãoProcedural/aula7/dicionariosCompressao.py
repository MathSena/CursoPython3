lista =[
    ('chave', 'valor'),
    ('chave1','valor1'),
]

#d1 = {x: y for x, y in lista}
d1 = dict(lista)
print(d1)

d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d2, type(d2))