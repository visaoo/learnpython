def phrase_count_dict(frase):
    dic = {}
    
    frase_split = frase.split()

    for char in frase_split:
        if char in dic:  # atribui +1 no dic caso a frase já exista
            dic[char] += 1
        else:  # caso contrario ele adiciona a frase ao dic
            dic[char] = 1
    return dic


frase = input("Escreva uma frase: ")
resultado = phrase_count_dict(frase)

print(resultado)
