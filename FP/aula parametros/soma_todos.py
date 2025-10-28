def soma_todos(*numeros):
    total = 0
    for n in numeros:
        total += n #p podemos total = total + n
    return total

print(soma_todos(1,2,3,4))  # Saída: 10