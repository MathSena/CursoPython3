def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

a = lambda x, y: x*y

print(a(2,2))


lista=[
    ['p1', 13],
    ['p2', 16],
    ['p3', 1],
    ['p4', 8],
    ['p5', 12],
]

def func(item):
    return item[1]

lista.sort(key=func)
print(lista)

lista.sort(key=lambda item: item[1])
print(lista)