while True:
    print()
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite um outro número: "))
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s] im ou [n] ão: ")

    if sair == 's':
        break
    else:
        if operador == '+':
            print(num_1 + num_2)
        elif operador == '-':
            print(num_1-num_2)
        elif operador == '/':
            print(num_1/num_2)
        elif operador == "*":
            print(num_1*num_2)


