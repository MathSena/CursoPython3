# Sets são conjuntos que suportam apenas elementos imutáveis
# Não existem indices, não respeitam ordem e não aceitam valores repetidos
s1 = {1,2,3,4,5,6}
print(s1)
for v in s1:
    print(v)

s1 = set()
print('Adicionando e removendo elementos')
s1.add(1) #Adicionando um elemento
s1.add(2)
s1.discard(2) #Removendo um elementoi
print(s1)

print('Adicionando e removendo elementos')
s1.update('Python')
print(s1)

print('Trasnformando uma lista em SET')
l1 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
l1 = set(l1) #CAST na lista como set
print(l1)
l1 = list(l1)
print('Trasnformando uma SET em lista')
print(l1)

print('Operação com conjuntos....')
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,7}
s3 = s1 | s2 #Union
print('Union')
print(s3)
print('Intersecção')
s3 = s1&s2#Intersecção
print(s3)
print('Diferença')
s3  = s2-s1 #Diferença
print(s3)


