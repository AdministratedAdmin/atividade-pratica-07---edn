import pandas as pd

arquivo = "atv/writenocsv.csv"

df = pd.read_csv(arquivo, encoding="utf-8")

print(df)