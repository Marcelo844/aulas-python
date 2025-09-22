import pandas as pd

df = pd.read_excel("dados.xlsx")
print("Ausentes por coluna (ANTES):")
print(df.isna().sum(), "\n")

df["Idade"] = df["Idade"].fillna(df["Idade"].mean())

df["Gasto Mensal"] = pd.to_numeric(df["Gasto Mensal"], errors="coerce")

df["Gasto Mensal"] = df["Gasto Mensal"].fillna(df["Gasto Mensal"].mean())

df["Gênero"] = df["Gênero"].fillna(df["Gênero"].mode()[0])

print("Valores ausentes depois do tratamento:")
print(df.isnull().sum())