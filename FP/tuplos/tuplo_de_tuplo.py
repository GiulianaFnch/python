# tuplo de tuplo
dados_pessoa = ("João", 25, "Rua das Flores", "Porto")

print("Dados originais da pessoa:", dados_pessoa)
print ("Nome:", dados_pessoa[0])
print("Idade:", dados_pessoa[1])
print("Morada:", dados_pessoa[2])
print("Cidade:", dados_pessoa[3])

# tentar alterar a cidade
try:
    dados_pessoa[3] = "Lisboa"
except TypeError as e:
    print("Erro:", e)
    
# solução: criar um novo tuplo com as alterações
morada_nova = ("Rua das Flores", "Lisboa")
dados_pessoa_novos = (dados_pessoa[0], dados_pessoa[1], morada_nova)
