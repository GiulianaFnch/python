# Função para calcular o valo total

def calcular_valor_total(preco_unitario, quantidade):
    valor_total = preco_unitario * quantidade
    return valor_total

# Entrada de dados do utilizador
preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo do valor total
valor_total = calcular_valor_total(preco_unitario, quantidade)

# Exibição do resultado, o f é string e .2f duas casas decimais, valor float
print(f"O valor total da compra é: R$ {valor_total:.2f}")
