# (Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de
# vogais e consoantes. Ignore espaços e caracteres especiais

frase = 'salve meu mano do caralho'


def conunt_vogais_consoantes(frase):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # inicio c > significado: counter
    c_vogais, c_consoantes = 0, 0
    
    for char in frase:
        if char in vogais:
            c_vogais += 1
        elif char in consoantes:
            print(char)
            c_consoantes += 1

    return c_vogais, c_consoantes


print(conunt_vogais_consoantes(frase))