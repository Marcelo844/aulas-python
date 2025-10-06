import pandas as pd
df = pd.read_excel("dados.xlsx")
antes = df.shape[0]
df.drop_duplicates(inplace=True)
depois = df.shape[0]

print(f"Removidas {antes - depois} linhas duplicadas")
print(df)