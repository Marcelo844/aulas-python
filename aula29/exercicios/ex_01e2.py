import pandas as pd

# Carregando o dataset
df = pd.read_excel("dados.xlsx")

# Primeiras linhas
print('Primeiras linhas do dataset:')
print(df.head())