"""
public, protected e private
"""

class BaseDados:
    def __init__(self): #Similiar a Construtor
        self.dados = {}


    def inserirDados(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})




bd = BaseDados()
bd.inserirDados(1, 'Matheus')
bd.inserirDados(2, 'Juliette')
bd.inserirDados(3, 'Gil')
print(bd.dados)