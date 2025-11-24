# Parte 1: Criação de listas

# criar listas de alunos e notas

nomes_alunos = []
notas_alunos = []

# exemplo de tupla com notas inseridas por engano
tupla_notas = (10,8,9)

# converter a tupla para listas para poder manipular
lista_notas = list(tupla_notas)

# Parte 2: Entrada de dados

# pedir ao utilizador para inserir 3 nomes e notas
for i in range(3):
    nome = input(f"Insira o nome do aluno {i+1}: ")
    nomes_alunos.append(nome)
    
    # pedir notas do aluno separadas por espaço
    notas_input= input(f"Insira as notas de {nome} separadas por espaço: "). split()
    
    #converter cada nota para inteiro usando map() e armazenar em lista
    notas_convertidas = list(map(int, notas_input))
    
    # adicionar as notas à lista principal de notas
    notas_alunos.append(notas_convertidas)
    
# Parte 3: criar um conjunto com todas as notas unicas

notas_unicas = set()

for notas in notas_alunos:
    for nota in notas:
        notas_unicas.add(nota)

print("Notas únicas:", notas_unicas)

# Parte 4: Calcular a média de cada aluno e criar dicionário

media_alunos = {}

# percorrer cada aluno e suas notas
for i in range(len(nomes_alunos)):
    nome = nomes_alunos[i]
    notas = notas_alunos[i]
    
    media = sum(notas) / len(notas) # calcular a média
    media_alunos[nome] = media # adicionar no dicionário (chave: nome, valor: média)
    

# Parte 5 : Exibir resultados

print("Média de cada aluno:")
for nome, media in media_alunos.items():
    print(f"{nome}: {media:.2f}")
    
# exibir o dicionário ocmpleto
print("Dicionário final:", media_alunos)