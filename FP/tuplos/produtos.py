produtos = ("arroz","feijão", "massa", "arroz", "leite", "massa")

for i in produtos:
    print ("Produto:", i)
    
input_produto = input ("Qual produto deseja procurar? ")

if input_produto in produtos:
    print (f"O produto {input_produto} está disponível.")
    print(f"O produto {input_produto} aparece {produtos.count(input_produto)} vez(es).")
    print(f"A primeira ocorrência do produto {input_produto} está na posição {produtos.index(input_produto)}.")
else:
    print (f"O produto {input_produto} não está disponível no tuplo.")