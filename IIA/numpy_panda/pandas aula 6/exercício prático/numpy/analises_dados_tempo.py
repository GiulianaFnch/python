import numpy as np

temperatures = np.random.randint(10, 35, size=(7,4))

print(temperatures)

# média do mês
print(np.mean(temperatures))

# dia mais frio
print(np.min(temperatures))

# dia mais quente
print(np.max(temperatures))

# Conte quantos dias tiveram temperaturas acima de 30°C
print(f"Temperaturas acima de 30°C: ", np.sum(temperatures >= 30))

# Crie uma máscara para extrair todos os dias em que a temperatura esteve entre 20°C e 25°C.
mask = (temperatures >= 20) & (temperatures <= 25)
print(f"Temperaturas entre 20°C e 25°C: ", temperatures[mask])