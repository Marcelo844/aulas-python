class Conta():
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    # Getter
    @property
    def saldo(self):
        return self.__saldo
    # Setter
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Não é possivel alterar o saldo")
        else:
            self.__saldo = valor

conta_um = Conta("Jonas", 100)
#O acesso ao getter e setter criados do jeito python se comportam como um acesso direto a variável
print(conta_um.saldo)
#Acesso ao setter
conta_um.saldo = 1000
#Acessando o getter
print(conta_um.saldo)