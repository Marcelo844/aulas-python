class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

pessoa_um = Pessoa("Jonas", 180)

print(pessoa_um.nome)
print(pessoa_um.altura)