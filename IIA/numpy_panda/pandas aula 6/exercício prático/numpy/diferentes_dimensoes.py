import numpy as np

sensor_1 = np.random.randint(0, 100, size=(10, 3))
# 10 linhas, 3 colunas

sensor_2 = np.random.randint(0, 100, size=(10,)) 
# 10 colunas, 1 linha

print (f"Sensor 1 dados:\n", sensor_1)
print (f"Sensor 2 dados:\n", sensor_2)

# adapte o formato do sensor 2 para ter mesmas dimensões do sensor 1
sensor_2_reshaped = sensor_2.reshape(10, 1)
print (f"Sensor 2 dados (reshape):\n", sensor_2_reshaped)

# soma elemento a elemento dos dois arrays
soma_sensores = sensor_1 + sensor_2_reshaped
print (f"Soma dos sensores:\n", soma_sensores)

# média de cada caracteristicas em todas as medicoes 
media_caracteristicas = np.mean(soma_sensores, axis=0) # media por coluna 
print (f"Média de cada característica:\n", media_caracteristicas)

# broadcasting para subtrair a media de cada coluna em sensor 1 ???? 
broadcasting = sensor_1 - media_caracteristicas
print (f"Sensor 1 broadcast:\n", broadcasting)