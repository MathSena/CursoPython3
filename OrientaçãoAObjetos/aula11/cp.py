from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self,valor):
        if self.saldo<valor:
            print('Saldo Insuficiente')
            return
        self.saldo -= valor
        self.detalhe()