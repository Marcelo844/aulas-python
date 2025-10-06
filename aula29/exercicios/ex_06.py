import pandas as pd

df = pd.read_excel("dados.xlsx")

mapa_genero = {
    "f": "F", "fem": "F", "feminino": "F",
    "m": "M", "masc": "M", "masculino": "M"
}
df["Gênero"] = (
    df["Gênero"]
    .astype(str).str.strip().str.lower()
    .map(mapa_genero)
    .fillna("F")  
)

df["Estado"] = df["Estado"].astype(str).str.strip().str.upper().str[:2]

print("Distribuição de Gênero:")
print(df["Gênero"].value_counts(dropna=False))
print("\nDistribuição de Estado:")
print(df["Estado"].value_counts(dropna=False))

print("\nAmostra:")
print(df.head(10))
