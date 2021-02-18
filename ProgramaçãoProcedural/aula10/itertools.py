"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Produto - Ordem importa e valores se repetem
"""

from itertools import combinations, permutations, product
print('Combinantions (Turno único)')
print()
times = ['Corinthians', 'Palmeiras', 'Santos,', 'São Paulo']

for game in combinations(times,2):
    print(game)

times_rio = ['Flamengo', 'Fluminense', 'Vasco', 'Botafogo']

print('Permutations (Turno e returno)')
print()
for game_rio in permutations(times_rio, 2):
    print(game_rio)

print('Product ')
print()

times_minas = ['Cruzeiro', 'Atlético Mineiro', 'América']

for game_minas in product(times_minas, repeat=2):
    print(game_minas)