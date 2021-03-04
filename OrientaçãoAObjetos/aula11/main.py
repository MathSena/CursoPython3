from OrientaçãoAObjetos.aula11.cp import ContaPoupanca
from OrientaçãoAObjetos.aula11.cc import ContaCorrente
print('Conta Poupança')
cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(100)
cp.sacar(5)
cp.sacar(100)

print('Conta Corrente')
cc = ContaCorrente(2222,3333,0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)