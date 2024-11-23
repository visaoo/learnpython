def char_count_dict(frase):
    dic = {}

    for char in frase:
        if char in dic:  # atribui +1 no dic caso o caractere já exista
            dic[char] += 1
        else:  # caso contrario ele adiciona a caractere ao dic
            dic[char] = 1
    return dic


frase = input("Escreva uma frase: ")
resultado = char_count_dict(frase)

print(resultado)
