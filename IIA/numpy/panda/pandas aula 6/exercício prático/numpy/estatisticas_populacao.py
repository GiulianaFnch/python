import numpy as np

np.random.seed(123)
population = np.array([120, 340, 230, 560, 190, 400, 310])

print(f"População: ",population)

# média da população
print(f"A média dessa população é: ",np.mean(population))

# mediana 
print(f"A mediana dessa população é: ",np.median(population))

# maior população
print(f"O maior valor dessa população é: ",np.max(population))

# percentagem que cada distrito representa no total da população
porcentagem_populacao = (population / population.sum()) * 100

print(f"A porcentagem de cada distrito é:\n", porcentagem_populacao)

# filtro para extrair distritos com populacao maior que 300 000 habitantes
mask = population > 300000
print(f"Distritos com população maior que 300.000 habitantes:\n", population[mask])