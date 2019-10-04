##### Funções #####
from aula3_ctaCorrente import Conta
from aula3_ctaPoupanca import Poupanca
from random import random, randrange

# CONTA CORRENTE
# Instanciando os objetos oConta e definindo o número de cada uma das contas
oConta1 = Conta(1)
oConta2 = Conta(2)

# Credito nas contas
oConta1.creditar(randrange(10))
oConta2.creditar(randrange(10))

# Consulta saldo das contas
print("Saldo da conta 1: ", oConta1.consultarSaldo())
print("Saldo da conta 2: ", oConta2.consultarSaldo())

# Transferencia de valor
oConta1.transferir(oConta2,randrange(10))

# Consulta saldo das contas
print("Saldo da conta 1 após as tranferência: ",  oConta1.consultarSaldo())
print("Saldo da conta 2 após as tranferência: ", oConta2.consultarSaldo())

oConta1.__saldo = 1000
print("Tentando alterar valor do saldo: ", oConta1.consultarSaldo())

#  CONTA POUPANCA
oCtaPoup1 = Poupanca(1)
print(oCtaPoup1.consultarSaldo())

oCtaPoup1.creditar(200.0)
print("Valor após creditar: ",oCtaPoup1.consultarSaldo())

oCtaPoup1.gerarRendimento(10)
print("Valor do rendimento: ",oCtaPoup1.consultaRendimento())

print("Saldo após o rendimento: ",oCtaPoup1.consultarSaldo())
