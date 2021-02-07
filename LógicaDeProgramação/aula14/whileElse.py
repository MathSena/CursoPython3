cont = 1
acum = 1

while cont<=10:
    print(cont, acum)

    if cont>5:
        break

    acum = acum +cont
    cont +=1
else:
    print('Cheguei no else')
print('Isso será executado')