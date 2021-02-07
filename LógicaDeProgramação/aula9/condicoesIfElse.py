"""
Condições IF, ELIF e Else
"""
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empéstimo')
else:
    print(f'{nome} não pode pegar o empréstimo')