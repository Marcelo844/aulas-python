import os
import pickle
import random
from dataclasses import dataclass, field

ARQ_CC = "contas_corrente.txt"
ARQ_CP = "contas_poupanca.txt"


def le_string(mensagem: str) -> str:
    return input(f"{mensagem}: ").strip()

def le_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(f"{mensagem}: ").strip())
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
def gera_identificador () -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(5))

@dataclass
class ContaBase:
    titular: str
    senha: str
    identificador: str = field(default_factory=gera_identificador)
    saldo: float = 0.0

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            print("Valor de depósito deve ser positivo.")
            return
        self.saldo += valor
    def valida_acesso(self, identificador: str, senha: str) -> bool:
        return self.identificador == identificador and self.senha == senha
    def set_senha(self, nova:str) -> None:
        self.senha = nova
    def verifica_saldo(self) -> str:
        return f"Seu saldo é: R$ {self.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

@dataclass
class ContaCorrente(ContaBase):
    limite: float = 0.0

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        return False
@dataclass
class ContaPoupanca(ContaBase):
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de saque deve ser positivo.")
            return False
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

def carregar_lista(caminho: str):
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "rb") as arquivo:
            lst = pickle.load(arquivo)
            return list(lst)
    except FileNotFoundError:
        print("Arquivo não encontrado!!")
    except Exception:
        print("Erro ao ler o arquivo")
    return[]

def salvar_lista(caminho: str, lista):
    try:
        with open(caminho, "wb") as salvar_arquivo:
            pickle.dump(lista, salvar_arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado!!")
    except Exception:
        print("Erro ao salvar o arquivo")

def acessa_cc(c1: ContaCorrente) -> ContaCorrente:
    print(f"Acessando conta corrente de {c1.identificador}")
    print(f"Bem Vindo!! {c1.titular}")
    while True:
        print("Selecione uma opção:")
        print("1 - Realizar um depósito")
        print("2 - Realizar um saque")
        print("3 - Verificar saldo")
        print("4 - Alterar senha")
        print("5 - Sair")
        opc = le_string("").lower()

        if opc == "1":
            valor = le_float("Digite o valor do depósito")
            c1.depositar(valor)
            print("Depósito realizado com sucesso!")
        elif opc == "2":
            valor = le_float("Digite o valor do saque")
            if c1.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque.")
        elif opc == "3":
            print(c1.verifica_saldo())
        elif opc == "4":
            nova_senha = le_string("Digite a nova senha")
            c1.set_senha(nova_senha)
            print("Senha alterada com sucesso!")
        elif opc == "5":
            print("Saindo da conta corrente.")
            break
    return c1

def acessa_cp(c2: ContaPoupanca) -> ContaPoupanca:
    print(f"Acessando conta poupança de {c2.identificador}")
    print(f"Bem Vindo!! {c2.titular}")
    while True:
        print("Selecione uma opção:")
        print("1 - Realizar um depósito")
        print("2 - Realizar um saque")
        print("3 - Verificar saldo")
        print("4 - Alterar senha")
        print("5 - Sair")
        opc = le_string("").lower()

        if opc == "1":
            valor = le_float("Digite o valor do depósito")
            c2.depositar(valor)
            print("Depósito realizado com sucesso!")
        elif opc == "2":
            valor = le_float("Digite o valor do saque")
            if c2.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente para saque.")
        elif opc == "3":
            print(c2.verifica_saldo())
        elif opc == "4":
            nova_senha = le_string("Digite a nova senha")
            c2.set_senha(nova_senha)
            print("Senha alterada com sucesso!")
        elif opc == "5":
            print("Saindo da conta poupança.")
            break
    return c2

def cadastro_cc() -> ContaCorrente:
    titular = le_string("Digite o nome do titular da conta corrente")
    senha = le_string("Digite a senha da conta corrente")
    limite = le_float("Digite o limite da conta corrente")
    c1 = ContaCorrente(titular=titular, senha=senha, limite=limite)
    print(f"Conta corrente criada com sucesso! Identificador: {c1.identificador}")
    return c1

def cadastro_cp() -> ContaPoupanca:
    titular = le_string("Digite o nome do titular da conta poupança")
    senha = le_string("Digite a senha da conta poupança")
    deposito = le_float("Digite o valor do depósito inicial")
    c2 = ContaPoupanca(titular=titular, senha=senha, saldo=deposito)
    print(f"Conta poupança criada com sucesso! Identificador: {c2.identificador}")
    return c2

def main():
    lista_cc = carregar_lista("contas_corrente.txt")
    lista_cp = carregar_lista("contas_poupanca.txt")
    cont_cc = len(lista_cc)
    cont_cp = len(lista_cp)

    while True:
        print("Selecione uma opção:")
        print("1 - Cadastrar Conta Corrente")
        print("2 - Cadastrar Conta Poupança")
        print("3 - Acessar Conta Corrente")
        print("4 - Acessar Conta Poupança")
        print("5 - Sair")
        opc = le_string("").lower()

        if opc == "1":
            lista_cc.append((cadastro_cc()))
            cont_cc += 1
        elif opc == "2":
            lista_cp.append((cadastro_cp()))
            cont_cp += 1
        elif opc == "3":
            identificador = le_string("Digite o identificador da conta corrente")
            senha = le_string("Digite a senha da conta corrente")
            pos = -1
            for i in range(cont_cc):
                if lista_cc[i].valida_acesso(identificador, senha):
                    pos = i
                    break
            if pos >= 0:
                lista_cc[pos] = acessa_cc(lista_cc[pos])
            else:
                print("Identificador ou senha inválidos para conta corrente.")
        elif opc == "4":
            identificador = le_string("Digite o identificador da conta poupança")
            senha = le_string("Digite a senha da conta poupança")
            pos = -1
            for i in range(cont_cp):
                if lista_cp[i].valida_acesso(identificador, senha):
                    pos = i
                    break
            if pos >= 0:
                lista_cp[pos] = acessa_cp(lista_cp[pos])
            else:
                print("Identificador ou senha inválidos para conta poupança.")
        elif opc == "5":
            salvar_lista("contas_corrente.txt", lista_cc)
            salvar_lista("contas_poupanca.txt", lista_cp)
            print("Saindo do sistema. Dados salvos com sucesso!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
        