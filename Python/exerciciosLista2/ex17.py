import random

numeros = [random.randint(-50, 50) for _ in range(5)]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Trocar os elementos se estiverem na ordem errada
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# or numeros.sort() >>>>>

numeros_ordenados = bubble_sort(numeros)
print(numeros_ordenados)  # [1, 2, 4, 5, 6, 9]
