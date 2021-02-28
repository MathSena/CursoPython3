from Escritor import Escritor
from Caneta import Caneta
from MaquinaDeEscrever import MaquinaDeEscrever

escritor =  Escritor('Napoleão Hill')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

