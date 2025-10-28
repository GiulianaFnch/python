import numpy as np

# colunas são produtos, linhas são dias da semana

sales = np.random.randint(50,500 ,size=(7,4))

print(f"Vendas semanais:\n{sales}")

# total de vendas de cada produto ao longo da semana
# 0 -> coluna - produtos
# 1 -> linhas - dias da semana
total_vendas_produto = sales.sum(axis=0)
print(f"Total de vendas dos produtos:\n{total_vendas_produto}")

# vendas diárias totais de todos os produtos
total_vendas_diarias = sales.sum(axis=1)
print(f"Total de vendas diárias:\n{total_vendas_diarias}")

# dia com maior volume de vendas
dia_maior_venda = np.argmax(total_vendas_diarias)
print(f"Dia com maior volume de vendas: Dia {dia_maior_venda + 1}")

# Use uma máscara booleana para encontrar os dias em que o total de vendas foi superior a 1200€. 

mask = total_vendas_diarias > 1200
dias_maior_1200 = np.where(mask)[0] + 1  # Adiciona 1 para ajustar o índice ao número do dia

print(f"Os dias com total de vendas maior que 1200€ foi: ",dias_maior_1200)