# Dicionário 1
dic1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

# Dicionário 2
dic2 = {
    'c': 30,
    'd': 40,
    'e': 50,
    'f': 60
}

dic3 = {}

for chave in dic1:
    if chave not in dic3:
        dic3[chave] = dic1[chave]

for chave in dic2:
    dic3[chave] = dic2[chave]
    if chave in dic1:
        dic3[chave] += dic1[chave]

print(dic3)
