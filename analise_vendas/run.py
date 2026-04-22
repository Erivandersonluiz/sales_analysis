import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Ler CSV
    df = pd.read_csv("vendas.csv")

    # Converter coluna de data
    df["data"] = pd.to_datetime(df["data"])
    df["receita"] = df["quantidade"] * df["preço"]

    # Total de vendas
    total_vendas = df["receita"].sum()

    # Vendas por produto
    vendas_por_produto = df.groupby("produto")["receita"].sum().sort_values(ascending=False)
    labels_produto = list(vendas_por_produto.index)
    values_produto = list(vendas_por_produto.values)

    # Vendas por mês
    df["mes"] = df["data"].dt.to_period("M").astype(str)
    vendas_por_mes = df.groupby("mes")["receita"].sum().sort_index()
    meses = list(vendas_por_mes.index)
    valores_mes = list(vendas_por_mes.values)

    # Produtos principais
    vendas_prod = df.groupby("produto").agg({
        "quantidade": "sum",
        "receita": "sum"
    })
    mais_vendido = vendas_prod["quantidade"].idxmax()
    quantidade_mais_vendido = int(vendas_prod.loc[mais_vendido, "quantidade"])
    maior_receita = vendas_prod["receita"].idxmax()
    valor_maior_receita = float(vendas_prod.loc[maior_receita, "receita"])

    return render_template(
        "dashboard.html",
        total_vendas=total_vendas,
        vendas_por_produto=vendas_por_produto.to_dict(),
        labels_produto=labels_produto,
        values_produto=values_produto,
        meses=meses,
        valores_mes=valores_mes,
        mais_vendido=mais_vendido,
        quantidade_mais_vendido=quantidade_mais_vendido,
        maior_receita=maior_receita,
        valor_maior_receita=valor_maior_receita
    )


if __name__ == "__main__":
    app.run(debug=True)
