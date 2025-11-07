import pandas as pd
import os

arquivo = "writenocsv.csv"

if not os.path.exists(arquivo):
    df = pd.DataFrame(columns=["Nome", "Idade", "Cidade"])
    df.to_csv(arquivo, index=False, encoding="utf-8")
    print("Arquivo criado")

while True:
    nome = input("Digite o nome ou ENTER para encerrar: ").strip()
    if nome == "":
        break

    idade = input("Digite a idade: ").strip()
    cidade = input("Digite a cidade: ").strip()

    updatedado = pd.DataFrame([[nome, idade, cidade]], columns=["Nome", "Idade", "Cidade"])

    updatedado.to_csv(arquivo, mode="a", header=False, index=False, encoding="utf-8")

    print("Salvo com sucesso!")


