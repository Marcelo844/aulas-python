#Herança de Classes
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        #Chamar o construtor da superclasse
        super().__init__(nome, idade)
        self.matricula = matricula
    def apresentar(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}')

aluno1 = Aluno("Maria", 20, "2024001")
aluno1.apresentar()