import random

poteA = []
poteB = []
poteC = []
poteD = []

a = int(input('Desejar continuar? (1) - SIM, (2) - Não: '))
add = str(input('Adicionar times em qual pote?:  '))

while a == 1:
    if add == 'A':
        if len(poteA) ==6:
            print('Times já adicionados! ')
            add = str(input('Adicionar times em qual pote?:  '))
        else:
            time = str(input('Digite o time: '))
            poteA.append(time)
            print(poteA)
            print('Faltam ', (6 - len(poteA),  ' times nessa lista'))

    if add == 'B':
        if len(poteB) ==8:
            print('Times já adicionados! ')
            add = str(input('Adicionar times em qual pote?:  '))
        else:
            time = str(input('Digite o time: '))
            poteB.append(time)
            print(poteB)
            print('Faltam ', (8 - len(poteB),  ' times nessa lista'))

#   if add == 'C':
#      if len(poteC) ==8:
#          print('Times já adicionados! ')
#          add = str(input('Adicionar times em qual pote?:  '))
#      else:
#          time = str(input('Digite o time: '))
#          poteC.append(time)
#          print(poteC)
#          print('Faltam ', (8 - len(poteC),  ' times nessa lista'))

#  if add == 'D':
#      if len(poteD) == 8:
#          print('Times já adicionados! ')
#          add = str(input('Adicionar times em qual pote?:  '))
#      else:
#          time = str(input('Digite o time: '))
#          poteD.append(time)
#          print(poteD)
#          print('Faltam ', (8 - len(poteD), ' times nessa lista'))

    if len(poteA) == 6 and len(poteB) == 8: # and len(poteC) == 8 and len(poteD) == 8:
        print(poteA)
        print(poteB)
        print(poteC)
        print(poteD)

        pote = str(input('Sorteio em qual pote? : '))

        if pote == 'A':
            sorteado = random.choice(poteA)
            print('O time sorteado é: ', sorteado)
            poteA.remove(sorteado)

        if pote == 'B':
            sorteado = random.choice(poteB)
            print('O time sorteado é: ', sorteado)
            poteB.remove(sorteado)


        if pote == 'C':
            sorteado = random.choice(poteC)
            print('O time sorteado é: ', sorteado)
            poteC.remove(sorteado)


        if pote == 'D':
            sorteado = random.choice(poteD)
            print('O time sorteado é: ', sorteado)
            poteD.remove(sorteado)


