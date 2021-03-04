from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return  self._saldo

    @saldo.setter
    def saldo(self,valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Salod precisa se rnúmerico")
        self._saldo = valor

    def depositar (self, valor):
        if not isinstance(valor, (int, float)):
             raise ValueError("Valor do deposíto precisa ser rnúmerico")
        self._saldo += valor
        self.detalhe()

    def detalhe(self):
        print(f'Agência: {self.agencia}', end=" ")
        print(f'Conta: {self.conta}', end=" ")
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass
