import json

# Nome do arquivo JSON
arquivo = 'json.json'

# Dados da pessoa
pessoa = {
    "nome": "Pedro",
    "idade": 30,
    "cidade": "São Paulo"
}

# --- Escrevendo os dados no arquivo JSON ---
with open(arquivo, 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

print("Dados gravados com sucesso!")

# --- Lendo os dados do arquivo JSON ---
with open(arquivo, 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)

print("Dados lidos do arquivo:")
print(dados_lidos)