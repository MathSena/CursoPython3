nome = "Matheus Sena"
idade = 24
altura = 1.70
e_maior = idade >18
peso = 55
imc = (peso/(altura*altura))

print(nome, " tem", idade, " e seu imc é de: ", imc)
print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')
print('{} tem {} anod de idade e seu imc é: {}'.format(nome, idade, imc))