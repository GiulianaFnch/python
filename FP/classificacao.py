#Solicitar o nome do utilizador
nome = input("Digite seu nome: ")

# Solicitar a classificação do utilizador
try:
    classificacao = float(input("Digite sua classificação (0 a 20): "))
    
    # Verificar se a classificação está dentro do intervalo de 0 a 20:
    if classificacao < 0 or classificacao > 20:
        print("Classificação inválida. Por favor, insira um valor entre 0 e 20.")
    else:
        #Verificar se a classificação é inferior a 10
        if classificacao < 10:
            falta = 10 - classificacao
            print(f"{nome}, falta-lhe {falta:.2f} pontos para atingir a classificação mínima de 10.")
        else:
            print(f"{nome}, parabéns! A classificação é {classificacao:.2f}, e é suficiente")

except ValueError:
    print("Erro. Por favor, insira uma valor numérico válido para a classificação.")

# Mostrar sempre a mensagem final
print("O programa vai terminar.")
