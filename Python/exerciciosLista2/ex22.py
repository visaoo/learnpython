# (Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de
# vogais e consoantes. Ignore espaços e caracteres especiais

frase = input('Digite uma frase: ')

def conunt_vogais_consoantes(frase): # função que conta vogais e consoantes
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    # inicio c > significado: counter
    c_vogais, c_consoantes = 0, 0

    for char in frase: # percorre a frase
        if char in vogais: # se o char está na vogais
            c_vogais += 1 # incrementa 1 c_vogais
        elif char in consoantes: # se o char está nas consoantes
            print(char)
            c_consoantes += 1 # incrementa 1 c_consoantes

    return c_vogais, c_consoantes, sum([c_vogais, c_consoantes]) # retorna a soma das vogais e consoantes, e a soma delas


c_vogais, c_consoantes, total = conunt_vogais_consoantes(frase) # chama a função
print(f'Vogais: {c_vogais}, Consoantes: {c_consoantes}')
print(f'Total de vogais e consoantes: {total}')