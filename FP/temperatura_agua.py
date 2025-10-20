# saber o estado da água com base na temperatura fornecida

nome = input("Digite seu nome: ")

temperatura = float(input("Digite a temperatura em graus Celsius: "))

# Estrutura de decisão para determinar o estado da água
if temperatura <= 0:
    estado = "sólido (gelo)"
elif temperatura >= 100:
    estado = "gasoso (vapor)"
else:
    estado = "líquido (água)"

print(f"{nome}, a água está em estado {estado} a {temperatura}°C.")

# exibir mensagem final
print("O programa vai terminar.")