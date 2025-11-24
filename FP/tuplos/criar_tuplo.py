numeros = (10,20,30)
print("Tuplo original:", numeros)

# tentar alterar vai causar erro ou seja o try e o except tratam o erro e mostram a mensagem sem parar o programa
try:
    numeros[1] = 99
except TypeError as e:
    print("Erro:", e)
    
# converter para lista para alterar
lista_temp = list(numeros)
lista_temp[1] = 99
lista_temp.append(40)  # adicionar um novo elemento

# converter de volta para tuplo
numeros = tuple(lista_temp)
print("Novo tuplo:", numeros)