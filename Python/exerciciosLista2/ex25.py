def num_par(x, y):
    lista_pares = []
    for i in range(x, y):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

def pedirNum(tipo):
    return int(input(f'Informe o valor {tipo}: '))

# Coletar os números iniciais e secundários
valor_inicial = pedirNum('inicial')
valor_secundario = pedirNum('secundário')

resultado = num_par(valor_inicial, valor_secundario)
print(f'Números pares do intervalo fornecido: {resultado}')