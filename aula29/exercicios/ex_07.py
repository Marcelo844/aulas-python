import pandas as pd
import numpy as np

df = pd.read_excel("dados.xlsx")

for col in ["Idade", "Gasto Mensal"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print("Estatísticas numéricas")
print(df.select_dtypes(include=[np.number]).describe())

cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
print("\nFrequências categóricas")
for col in cat_cols:
    print(f"\nColuna: {col}")
    print(df[col].value_counts(dropna=False))