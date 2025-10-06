import pandas as pd

df = pd.read_excel("dados.xlsx")

df = df.drop_duplicates()

df.to_csv("dados_limpos.csv", index=False, encoding="utf-8-sig")

print("Salvo como: dados_limpos.csv")
print("\nAmostra do que foi salvo:")
print(df.head(10))