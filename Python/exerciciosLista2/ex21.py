lista = [40, 20, 30, 20, 20, 20, 50, 60, 10, 50, 50, 10] # lista original

def list_corret(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

r = list_corret(lista)
print(r) # lista modificada
