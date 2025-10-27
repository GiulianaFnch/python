# Função que retorna múltiplos valores

def operacoes(a,b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return soma, sub, mult, div 

# Chmada da função e desempacotamento dos valores retornados
s, sub, mult, div = operacoes(10, 5)

print(f"Soma: {s}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
