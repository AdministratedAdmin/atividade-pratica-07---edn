import pandas as pd

# Não entendi/encontrei dados de log de ML. Utilizei tempo de processamento de alguns processadores
arquivo = "dataset.csv"

dados = pd.read_csv(arquivo)

media = dados["time"].mean()
desvio_padrao = dados["time"].std()

print(f"Média do tempo de execução: {media:.2f}")
print(f"Desvio padrão: {desvio_padrao:.2f}")