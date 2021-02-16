string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

n=10
cont = [i for i in range (0, len(string), n)]
tuplas = [(i, i+n) for i in range(0, len(string), n)]
lista = [string[i:i+n] for i in range(0, len(string),n)]
retorno = '.'.join(lista)

print(cont)
print(tuplas)
print(lista)
print(retorno)
