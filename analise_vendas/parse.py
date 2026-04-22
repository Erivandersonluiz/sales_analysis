import pandas as pd
import matplotlib.pyplot as plt

# Ler o CSV
df = pd.read_csv("vendas.csv")

# Converter coluna 'data' para datetime
df['data'] = pd.to_datetime(df['data'])

# Criar coluna de mês
df['mes'] = df['data'].dt.to_period('M')

# Calcular vendas por mês (receita)
vendas_por_mes = df.groupby('mes').apply(lambda d: (d['quantidade'] * d['preço']).sum())

# Resetar índice para facilitar manipulação
vendas_por_mes = vendas_por_mes.reset_index()
vendas_por_mes.columns = ['mes', 'receita']

print("Vendas por mês:")
print(vendas_por_mes)

# Calcular vendas por produto
df['receita'] = df['quantidade'] * df['preço']

vendas_prod = df.groupby('produto').agg({
    'quantidade': 'sum',
    'receita': 'sum'
})

# Encontrar produtos mais vendidos
mais_vendido = vendas_prod['quantidade'].idxmax()
mais_receita = vendas_prod['receita'].idxmax()

print(f"Produto mais vendido em unidades: {mais_vendido} (total {vendas_prod.loc[mais_vendido, 'quantidade']})")
print(f"Produto com maior receita: {mais_receita} (total R$ {vendas_prod.loc[mais_receita, 'receita']:.2f})")

# Preparar dados para gráfico
vendas_por_mes['mes'] = vendas_por_mes['mes'].astype(str)

plt.figure(figsize=(10, 6))
vendas_por_mes.plot(x='mes', y='receita', kind='bar')
plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()