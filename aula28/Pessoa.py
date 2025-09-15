class Pessoa:
    #Constructor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

pessoa1 = Pessoa('Alice', 30)
pessoa1.apresentar()