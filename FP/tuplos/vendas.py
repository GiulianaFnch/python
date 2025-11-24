# criar tuplos mes vendas

vendas = (
    ("Janeiro", 1500),
    ("Fevereiro", 1800),
    ("Março", 2200),
    ("Abril", 1700),
    ("Maio", 2000),
    ("Junho", 2500),
)

# mostrar as vendas
print("=== Relatório de Vendas ===")
for mes, valor in vendas:
    print(f"Mês: {mes}, Vendas: €{valor}")

# calcular total anual e média 
total_vendas = sum(valor for _, valor in vendas)
media_mensal = total_vendas / len(vendas)

print(f"Total anual de vendas: €{total_vendas}")
print(f"Média mensal de vendas: €{media_mensal:.2f}")

# mes com mais e menos vendas
melhor_mes = max(vendas, key=lambda v: v[1])
pior_mes = min(vendas, key=lambda v: v[1]) 

print(f"Melhor mês: {melhor_mes[0]} com vendas de €{melhor_mes[1]}")
print(f"Pior mês: {pior_mes[0]} com vendas de €{pior_mes[1]}")