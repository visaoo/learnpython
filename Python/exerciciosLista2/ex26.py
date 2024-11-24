# Dicionário 1
dic1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

# Dicionário 2
dic2 = {
    'a': 2,
    'c': 30,
    'd': 40,
    'e': 50,
    'f': 60
}

# Dicionário 3

def mesclarDic(dic1, dic2):
    dic3 = dic1.copy()

    for chave, valor in dic2.items():  # puxa as keys e values do dic2
        if chave not in dic3:
            # caso o valor não exista dentro do dic3 ele "adiciona"
            dic3[chave] = valor
        else:
            dic3[chave] += valor  # caso o valor já exista ele incrementa

    return dic3

resultado = mesclarDic(dic1, dic2)

print(resultado)
