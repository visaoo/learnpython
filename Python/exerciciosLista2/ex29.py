def removerDuplicados(lista_aninhada):
    lista_nova = []
    for sublista in lista_aninhada:
        # transformando em arr e removedo as duplicatas
        sublistaUn_ = list(set(sublista))
        lista_nova.append(sublistaUn_)
        # print(list(lista_nova))  # list transforma o obj in arr
    return lista_nova


lista_aninhada = [[1, 2, 2, 3, 4, 4, 5], [
    4, 4, 4, 6, 6, 7, 8], [1, 1, 2, 2, 3, 3, 4]]

lista_nova = removerDuplicados(lista_aninhada)
print(lista_nova)
