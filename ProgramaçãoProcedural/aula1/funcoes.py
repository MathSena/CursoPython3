def funcao():
    print("Hello world")

funcao()
funcao()
funcao()
funcao()

def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)

saudacao()
saudacao("Olá", "Matheus!")
saudacao('Luiz')
saudacao('', 'Alberto')


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1/n2


divide = divisao(9,0)

if divide:
    print(divide)
else:
    print("Conta inválida")