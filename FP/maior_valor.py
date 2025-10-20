# Solicitar o nome ao utilizador dois valores númericos e dizer qual o maior dos dois

nome = input("Digite seu nome: ")
valor1 = float(input("Digite o primeiro valor numérico: "))
valor2 = float(input("Digite o segundo valor numérico: "))

if valor1 > valor2:
    print(f"{nome}, o maior valor entre {valor1} e {valor2} é {valor1}.")
elif valor2 > valor1:
    print(f"{nome}, o maior valor entre {valor1} e {valor2} é {valor2}.")
else:
    print(f"{nome}, os dois valores são iguais: {valor1}.")

print("O programa vai terminar.")