from itertools import zip_longest, count
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Curitiba', 'Porto Alegre']
estados = ['SP', 'MG', 'BA', 'PR']

cidades_estados = zip(
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)