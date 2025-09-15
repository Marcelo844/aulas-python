def mostra_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
        
mostra_info(nome="Alice", idade=30, cidade="São Paulo")