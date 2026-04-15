import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Ler CSV
    df = pd.read_csv("vendas.csv")

    # Receita total
    df["receita"] = df["quantidade"] * df["preço"]
    total_vendas = df["receita"].sum()

    # Vendas por produto
    vendas_por_produto = df.groupby("produto")["receita"].sum().to_dict()

    # Preparar dados para gráfico
    labels = list(vendas_por_produto.keys())
    values = list(vendas_por_produto.values())

    return render_template(
        "dashboard.html",
        total_vendas=total_vendas,
        labels=labels,
        values=values
    )

if __name__ == "__main__":
    app.run(debug=True)
