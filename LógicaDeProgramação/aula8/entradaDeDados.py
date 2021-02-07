"""
Input é uma função que recebe dados digitados
"""

nome = input("Qual o seu nome? ")

print(f'O usuário digitou {nome} e o tipo da variável é'
      f'{type(nome)}')


num1 = int(input("Digite um número: "))
num2 = input("Digite outro número: ")
num2 = int(num2)


print("A some é: ", (num1+num2))

