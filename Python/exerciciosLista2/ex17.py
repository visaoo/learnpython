import random

numeros = [random.randint(-50, 50) for _ in range(5)]
# Desordenados
print(numeros)
# Ordenando
numeros.sort()

print(numeros)

