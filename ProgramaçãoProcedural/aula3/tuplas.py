#Não consigo alterar elementos de tuplas

t1 = (1,2,3, 'a', 'Luiz Otávio')


print(t1[4])


for v in t1:
    print(v)


t2 = (1,2,3,4,5)
t2 = list(t2)
print('Tupla antes de alterar valor: ', t2)
t2[1] = 3000
t2 = tuple(t2)
print('Tupla depois de  alterar valor: ', t2)




