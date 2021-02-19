try:
    a=0
    try:
        a=1/0
    except:
        print('Erro')

except NameError as erro:
    print("Erro do dev", erro)
except (IndexError, KeyError) as erro:
    print("Erro do índice ou chave")
except Exception as erro:
    print("Erro inesperado")
else:
    pass
finally:
    a = ''

print(a)
