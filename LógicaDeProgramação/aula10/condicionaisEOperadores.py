"""
Operadores lógicos + IF/ELSE
"""

usuario = input("Nome do usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = "Luiz"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("Vocês está logado")
else:
    print("Usuário ou senha inválidos")