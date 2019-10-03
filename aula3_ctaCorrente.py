##### Funções #####
# Variaveis privadas

from random import random, randrange

class Conta:

    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0

    def consultarSaldo(self):
        return self.__saldo
    
    def creditar(self, credval):
        self.__saldo += credval

    def debitar(self, debitval):
        self.__saldo -= debitval
    
    def transferir(self, conta, transfval):
        if transfval > 0:    
            if self.__saldo > 0 and self.__saldo >= transfval:
                self.__saldo -= transfval
                conta.__saldo += transfval
                print("Valor transferido: ", transfval)
            else:
                print("Saldo insdisponível")
        else:
            print("Não foi feita nenhuma transferencia")

class Poupanca(Conta):
    
    def __init__(self, numero):
        super().__init__(numero)
        self.__rendimento = 0.0
    
    def consultaRendimento(self):
        return self.__rendimento

    def gerarRendimento(self, taxa):
        self.__rendimento += super().consultarSaldo() * taxa / 100

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
