from calculadora import soma

try:
    print(soma(10, '10'))
except AssertionError as e:
    print(f'Conta inválida: {e}')
