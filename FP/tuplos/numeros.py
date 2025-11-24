numeros = (5,8,2,10,3,1,6,13,2,45,8,41,4,27)

for i in numeros:
    print(i)
    
print("O maior número é:", max(numeros))
print("O menor número é:", min(numeros))

soma = sum(numeros)
media = soma / len(numeros)
print("A soma dos números é:", soma)
print("A média dos números é:", media)


print("\nNúmeros pares: ")
for i in numeros:
    if i%2 == 0:
        print(i)