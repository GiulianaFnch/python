# soliticitar ao utilizador um numero de 1 a 7

dia = int(input("Digite um número de 1 a 7 para o dia da semana correspondente: "))

if dia == 1:
    dia_semana = "Domingo"
elif dia == 2:
    dia_semana = "Segunda-feira"
elif dia == 3:
    dia_semana = "Terça-feira"  
elif dia == 4:
    dia_semana = "Quarta-feira"
elif dia == 5:
    dia_semana = "Quinta-feira"
elif dia == 6:
    dia_semana = "Sexta-feira"
elif dia == 7:
    dia_semana = "Sábado"
else:
    dia_semana = "Número inválido. Por favor, insira um número entre 1 e 7."
# exibir resultado

print(f"O dia correspondente ao número {dia} é: {dia_semana}.")

print ("O programa vai terminar.")