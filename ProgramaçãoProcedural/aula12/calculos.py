import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica_lista(lista):
    r = 1
    for i in lista:
        r *= i
    return r

if __name__ == '__main__': #Se esse módulo for igual a main, executa o resto
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica_lista(lista))
    print(PI)