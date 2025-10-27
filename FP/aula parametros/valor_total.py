# calcular o valor total de um produto dados o preço unitario e quantidade do mesmo

preco_unitario = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

def valor_total(preco_unitario, quantidade):
    return preco_unitario * quantidade

total = valor_total(preco_unitario, quantidade)
print(f"O valor total é: {total:.2f}€")