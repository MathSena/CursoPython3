
import json
d1={
    'Pessoa 1': {
    'nome': 'Juliette',
    'idade': 31,
},
    'Pessoa 2': {
        'nome': 'Gil',
        'idade': 28,
},
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)