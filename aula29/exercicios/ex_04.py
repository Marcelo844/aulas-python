import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)

df = pd.read_excel("dados.xlsx")

df["Idade"] = pd.to_numeric(df["Idade"], errors="coerce").astype("Int64")

df["Gasto Mensal"] = pd.to_numeric(df["Gasto Mensal"], errors="coerce")

df["Data de Cadastro"] = pd.to_datetime(df["Data de Cadastro"], errors="coerce")

print("Tipos de dados após a conversão:")
print(df.dtypes)