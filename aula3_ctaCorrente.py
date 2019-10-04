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

