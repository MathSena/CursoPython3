usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres<6:
    print("Você precisa digitar ao menos 6 caracteres:")
else:
    print("Você foi cadastrado no sistema")