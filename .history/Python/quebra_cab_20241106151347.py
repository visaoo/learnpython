# arr = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]

# # for i in range(0, 4):
# #     print(i) # exibi numero por numero até o 3
    
# print(arr[0])
# # for i in arr[0]:
#     # print(i)
#     # print(arr[0][i-1])
# Jogo da forca

# palavra[i] = l # pode usar o l ou chute

# certos = count(start=0, step=1) posso usar o next(contador) assim posso pegar o prox numero

from random import choice


lista_de_frutas = ["maçã", "banana", "laranja", "manga", "morango", "uva", "abacaxi", "kiwi"]
palavra_secreta = choice(lista_de_frutas)


letras_digitadas = []
def verifica_acerto(palavra, chute, result = False):
    letras_digitadas.append(chute)
    for i, l in enumerate(palavra):
        if l == chute:
            result = not result
        
    return result


def gerar_andelaine(palavra):
    arr = ['_' for _ in palavra]
    return arr 

# def insertLetra(letra, palavra, result = ''):
    
#     return result






# se_matou = enforcou = False


# se_matou = enforcou = False
# letras_digitadas = []
# forca = ...

# while not se_matou and not enforcou:
#     se_matou = True
#     forca = len(palavra_secreta[0])
#     forca = forca * '_'
#     print(forca)
    # chute = input('Digite uma letra... ').lower()
    
    # for i, letra in enumerate(palavra_secreta[0]):
    #     if letra == letras_digitadas[i]:
    #         print('Você já digitou essa letra tente novamente.')
            
    #     if chute == letra:
    #         palavra_secreta[0] = chute
    #         print(chute)
    
