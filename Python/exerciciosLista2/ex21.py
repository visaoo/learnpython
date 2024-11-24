lista = [40, 20, 30, 20, 20, 20, 50, 60, 10, 50, 50, 10] # lista original

def list_corret(lista):
    nova_lista = list(set(lista))
    return nova_lista

r = list_corret(lista)
# print(lista) # orig 
print(r) # mod