def mostra_info(**info):
    ''''Mostra informações passadas como argumentos nomeados.'''
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
        
mostra_info(nome="Alice", idade=30, cidade="São Paulo")

print(mostra_info.__doc__)