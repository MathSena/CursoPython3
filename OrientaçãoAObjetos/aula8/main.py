from classes import *

"""
Associação - > Usa
Agregação -> Tem
Composição -> Dono
Herança -> É
"""

c1 = Cliente('Sarah', 28)
c1.falar()
c1.comprar()
c1.estudar()

a1 = Aluno('Juliette', 31)
a1.falar()
a1.estudar()
a1.comprar()