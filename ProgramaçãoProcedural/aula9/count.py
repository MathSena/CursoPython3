from itertools import count

contador = count(start=-1, step=-1)

conta = 0

for valor in contador:
    print(round(valor, 7))

    if valor >= 10 or valor <=-10:
        break