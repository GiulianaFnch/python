import pandas as pd
import numpy as np

date = pd.date_range(start="20240101", end="20241231")

category = np.random.choice(["Eletrónicos", "Roupas", "Alimentos"], len(date))

product = [
    (
        np.random.choice(["TV", "Notebook", "Tablet"])
        if i == "Eletrónicos"
        else (
            np.random.choice(["Camisa", "Calças", "Vestido", "Blusa"])
            if i == "Roupas"
            else np.random.choice(["Arroz", "Feijão", "Açúcar"])
        )
    )
    for i in category
]

value = np.random.randint(50, 1500, size=len(date))
df = pd.DataFrame(
    {"data": date, "categoria": category, "producto": product, "valor": value}
)

print(df.head())

# 1. Calcule o total de vendas por categoria.

# agrupa pela coluna 'categoria' e soma os valores da coluna 'valor'
totais_pd = df.groupby("categoria")["valor"].agg("sum")
print(f"\nTotal de vendas por categoria:\n", totais_pd)

# 2. Calcule a média de vendas por produto.

media_vendas = df.groupby("producto")["valor"].agg("mean")
print(f"\nMédia de vendas por produto:\n", media_vendas)

# 3. Identifique a categoria com maior volume total de vendas.

categoria_max = totais_pd.idxmax()    # rótulo (ex.: 'Eletrónicos') 
valor_max = totais_pd.max()           # valor numérico do total

print(f"Categoria com maior volume: {categoria_max} ({valor_max})")

# 4. Crie uma tabela pivot com as categorias como linhas, as datas como colunas e a soma dos valores de venda como valores.

tabela_pivot = df.pivot_table(values="valor", index="categoria", columns="data", aggfunc="sum", fill_value=0)

print(f"Tabela pivot: \n", tabela_pivot)

