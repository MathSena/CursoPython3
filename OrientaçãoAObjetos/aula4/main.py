"""
public, protected e private
_ -> protected
__ ->private
"""

class BaseDados:
    def __init__(self): #Similiar a Construtor
        self._dados = {}

    def inserirDados(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def listaCLientes(self):
        for id, nome in self._dados['clientes'].itens():
            print(id, nome)

    def apagaCliente(self, id):
        del self._dados['clientes'][id]




bd = BaseDados()
bd.inserirDados(1, 'Matheus')
bd.inserirDados(2, 'Juliette')
bd.inserirDados(3, 'Gil')
print(bd._dados)