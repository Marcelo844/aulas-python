# Variável Global
x = 10

def soma(valor):
    # Acessando a variável global
    global x
    x+= valor+10
    print(x)

soma(5)