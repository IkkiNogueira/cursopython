##### Funções #####

from random import random, randrange

class Conta:

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

    def consultarSaldo(self):
        return self.saldo
    
    def creditar(self, credval):
        self.saldo += credval

    def debitar(self, debitval):
        self.saldo -= debitval
    
    def transferir(self, conta, transfval):
        if transfval > 0:    
            if self.saldo > 0 and self.saldo >= transfval:
                self.saldo -= transfval
                conta.saldo += transfval
                print("Valor transferido: ", transfval)
            else:
                print(transfval, "Saldo insdisponível")
        else:
            print("Não foi feita nenhuma transferencia")

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
