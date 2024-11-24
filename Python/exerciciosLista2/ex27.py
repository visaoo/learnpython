def phrase_count_dict(frase):
    dic = {} # cria um dicionario
    
    frase_split = frase.split()

    for char in frase_split:
        if char in dic:  # atribui +1 no dic caso a frase já exista
            dic[char] += 1 # atribui +1 no dic caso a frase já exista
        else:  # caso contrario ele adiciona a frase ao dic
            dic[char] = 1 # se não ele adiciona a frase ao dic
    return dic


frase = input("Escreva uma frase: ")
resultado = phrase_count_dict(frase)

print(resultado)
