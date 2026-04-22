import pandas as pd

# Criando dados sintéticos
dados = {
    "data": ["2025-01-05", "2025-01-20", "2025-02-13", "2025-02-25", "2025-03-10"],
    "produto": ["A", "B", "A", "C", "B"],
    "quantidade": [3, 1, 2, 5, 4],
    "preço": [10.0, 20.0, 10.0, 15.0, 20.0]
}

df = pd.DataFrame(dados)

# Exportando para CSV
df.to_csv("vendas.csv", index=False)

print("Arquivo vendas.csv criado com sucesso!")
