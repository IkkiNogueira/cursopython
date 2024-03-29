from aula3_ctaCorrente import Conta

class Poupanca(Conta):
    
    def __init__(self, numero):
        super().__init__(numero)
        self.__rendimento = 0.0
    
    def consultaRendimento(self):
        return self.__rendimento

    def gerarRendimento(self, taxa):
        self.__rendimento += super().consultarSaldo() * taxa / 100

    def consultarSaldo(self):
        return super().consultarSaldo() + self.__rendimento
