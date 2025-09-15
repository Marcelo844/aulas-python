class Conta:
    titular: str
    saldo: float
    operacoes: list[str]

conta_um = Conta()
conta_um.titular = "Marcelo"
conta_um.saldo = 20

print(conta_um.titular)
print(conta_um.saldo)