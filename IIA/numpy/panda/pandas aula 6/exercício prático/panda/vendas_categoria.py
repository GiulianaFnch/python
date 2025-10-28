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