import time
print('Iteradores')
lista = [0,1,2,3,4,5]

print('Verificando se a lista é um interador...')
print(hasattr(lista, '__next__'))
print('Transformando a lista é um interador com o metódo iter..')
lista = iter(lista)
print(hasattr(lista, '__next__'))
print('O laço for transforma a lista em um interador')
for v in lista:
    print(v)

print('Gerador')

def gera():
    for i in range(100):
        yield i
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)

    