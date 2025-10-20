# solicitar ao utilizador quantos números ele quer inserir
n = int(input("Quantos números você deseja inserir para calcular a média? "))

# inicializar a variavel para somar os números
soma = 0

# utilizar um ciclo for para obter os números e calcular a soma
for i in range(n):
    numero = int(input(f"Digite o número {i + 1}º número: "))
    soma += numero

# calcular a média
if n > 0:
    media = soma / n
    # exibir o resultado
    print(f"A média dos {n} números inseridos é: {media:.2f}")
else:
    print("Nenhum número foi inserido")

# exibir mensagem final
print("O programa vai terminar.")