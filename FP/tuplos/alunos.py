# Criar tuplos com dados dos alunos (nome, idade, nota)

aluno1 = ("João",20,15.5)
aluno2 = ("Maria",22,18.0)
aluno3 = ("Ana",19,17.2)
aluno4 = ("Pedro",21,12.8)

# colocar todos os alunos dentro de um tuplo de tuplos
turma = (aluno1, aluno2, aluno3, aluno4)

# mostrar todos os alunos
for aluno in turma:
    nome, idade, nota = aluno # desempacotar o tuplo
    print(f"Nome: {nome}, Idade: {idade}, Nota: {nota}")

# calcular a média das notas
soma_notas = sum(aluno[2] for aluno in turma)
media = soma_notas / len(turma)
print(f"Média das notas: {media:.2f}")

# encontrar o aluno com a maior nota
melhor_aluno = max(turma, key=lambda aluno: aluno[2]) # compara pela nota
print(f"Melhor aluno: {melhor_aluno[0]} com nota {melhor_aluno[2]}")

# encontrar o aluno com menor nota
pior_aluno = min(turma, key=lambda aluno: aluno[2]) 

print(f"Pior aluno: {pior_aluno[0]} com nota {pior_aluno[2]}")