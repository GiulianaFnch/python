'''
Largest City: Given a dict of city populations,
print the city with the largest population.
'''

cidade = { "Lisboa" : 1098200, "Porto" : 500591, "Vila Real" : 49779, "Viseu" : 2000111 }

maior_cidade = max(cidade, key=cidade.get)
print ("Maior cidade ", maior_cidade)