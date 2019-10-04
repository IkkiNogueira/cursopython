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
