# funções lambda (anônimas)

# função de uma linha
dobro = lambda x: x * 2

print(dobro(5))  # saída: 10

# Pode ser usada em listas

numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # saída: [2, 4, 6, 8]