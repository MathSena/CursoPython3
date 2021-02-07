frase = 'O palmeiras não tem mundial'
tamanho_frase = len(frase)
contador = 0
nova_string = ' '

user = input('Qual letra colocar em maiúscula? ')

while contador<tamanho_frase:
    letra = frase[contador]
    if letra == user:
        nova_string += user.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
