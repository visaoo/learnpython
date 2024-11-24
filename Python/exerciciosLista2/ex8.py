lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def genList (arr):
    return len(arr), sum(arr)

tam, soma = genList(lista)

print(tam)
print(soma)